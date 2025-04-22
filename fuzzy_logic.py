import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define typical power consumption and default usage hours for appliances
APPLIANCE_DATA = {
    'fan': {
        'power': 75,  # Ceiling fan
        'default_hours': 8,  # Default hours of usage
        'max_hours': 24  # Max possible hours
    },
    'light': {
        'power': 40,  # LED bulb average
        'default_hours': 6,
        'max_hours': 16
    },
    'fridge': {
        'power': 150,  # Regular refrigerator
        'default_hours': 24,  # Runs all day
        'max_hours': 24
    },
    'ac': {
        'power': 1500,  # 1.5 ton AC
        'default_hours': 6,
        'max_hours': 12
    },
    'tv': {
        'power': 100,  # LED TV
        'default_hours': 4,
        'max_hours': 16
    },
    'washing_machine': {
        'power': 500,
        'default_hours': 2,
        'max_hours': 4
    },
    'microwave': {
        'power': 800,
        'default_hours': 1,
        'max_hours': 3
    },
    'computer': {
        'power': 150,
        'default_hours': 4,
        'max_hours': 12
    },
    'water_heater': {
        'power': 2000,
        'default_hours': 1,
        'max_hours': 3
    },
    'iron': {
        'power': 1000,
        'default_hours': 1,
        'max_hours': 3
    }
}

def calculate_actual_consumption(appliances, appliance_hours):
    """Calculate actual consumption based on appliance power ratings and individual usage hours"""
    daily_consumption = sum(
        count * APPLIANCE_DATA[app]['power'] * hours / 1000  # Convert to kWh
        for app, count in appliances.items()
        for hours in [appliance_hours.get(app, APPLIANCE_DATA[app]['default_hours'])]
        if app in APPLIANCE_DATA and count > 0
    )
    return daily_consumption

def validate_hours(app, hours):
    """Validate that the hours are within acceptable range for the appliance"""
    if app not in APPLIANCE_DATA:
        return APPLIANCE_DATA['fan']['default_hours']  # Use fan as default
    max_hours = APPLIANCE_DATA[app]['max_hours']
    if hours is None or hours < 0:
        return APPLIANCE_DATA[app]['default_hours']
    return min(hours, max_hours)

def create_fuzzy_system():
    # Input variables
    appliances = ctrl.Antecedent(np.arange(0, 21, 1), 'appliances')
    usage_hours = ctrl.Antecedent(np.arange(0, 25, 1), 'usage_hours')
    season = ctrl.Antecedent(np.arange(0, 3, 1), 'season')
    
    # Output variable - adjusted to more realistic range for tier 3 city home
    consumption = ctrl.Consequent(np.arange(0, 21, 1), 'consumption')

    # Membership functions for appliances with realistic categorization
    appliances['very_low'] = fuzz.trimf(appliances.universe, [0, 0, 5])
    appliances['low'] = fuzz.trimf(appliances.universe, [3, 6, 9])
    appliances['medium'] = fuzz.trimf(appliances.universe, [7, 10, 13])
    appliances['high'] = fuzz.trimf(appliances.universe, [11, 14, 17])
    appliances['very_high'] = fuzz.trimf(appliances.universe, [15, 20, 20])

    # Membership functions for usage hours
    usage_hours['very_low'] = fuzz.trimf(usage_hours.universe, [0, 0, 6])
    usage_hours['low'] = fuzz.trimf(usage_hours.universe, [4, 8, 12])
    usage_hours['medium'] = fuzz.trimf(usage_hours.universe, [10, 14, 18])
    usage_hours['high'] = fuzz.trimf(usage_hours.universe, [16, 20, 24])

    # Membership functions for season
    season['winter'] = fuzz.trimf(season.universe, [0, 0, 1])
    season['monsoon'] = fuzz.trimf(season.universe, [0, 1, 2])
    season['summer'] = fuzz.trimf(season.universe, [1, 2, 2])

    # Membership functions for consumption (kWh per day)
    consumption['very_low'] = fuzz.trimf(consumption.universe, [0, 2, 4])
    consumption['low'] = fuzz.trimf(consumption.universe, [3, 5, 7])
    consumption['medium'] = fuzz.trimf(consumption.universe, [6, 9, 12])
    consumption['high'] = fuzz.trimf(consumption.universe, [10, 14, 17])
    consumption['very_high'] = fuzz.trimf(consumption.universe, [15, 18, 20])

    # Rules remain same as before
    rules = [
        # Basic usage patterns
        ctrl.Rule(appliances['very_low'], consumption['very_low']),
        ctrl.Rule(appliances['low'] & usage_hours['low'], consumption['very_low']),
        ctrl.Rule(appliances['low'] & usage_hours['medium'], consumption['low']),
        
        # Medium household
        ctrl.Rule(appliances['medium'] & usage_hours['medium'] & season['winter'], consumption['low']),
        ctrl.Rule(appliances['medium'] & usage_hours['medium'] & season['monsoon'], consumption['medium']),
        ctrl.Rule(appliances['medium'] & usage_hours['medium'] & season['summer'], consumption['medium']),
        
        # AC usage patterns
        ctrl.Rule(appliances['high'] & season['summer'] & usage_hours['high'], consumption['high']),
        ctrl.Rule(appliances['high'] & season['summer'] & usage_hours['medium'], consumption['medium']),
        ctrl.Rule(appliances['high'] & season['winter'], consumption['low']),
        
        # Heavy usage
        ctrl.Rule(appliances['very_high'] & usage_hours['high'] & season['summer'], consumption['very_high']),
        ctrl.Rule(appliances['very_high'] & season['winter'], consumption['medium']),
        
        # Season specific
        ctrl.Rule(season['summer'] & usage_hours['high'], consumption['high']),
        ctrl.Rule(season['winter'] & usage_hours['high'], consumption['medium']),
        ctrl.Rule(season['monsoon'] & usage_hours['medium'], consumption['medium'])
    ]

    system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(system)

def predict_consumption(appliance_dict, appliance_hours, season_val):
    """
    Predict consumption using both fuzzy logic and actual power ratings
    """
    if not isinstance(season_val, (int, float)):
        raise ValueError("Season must be a number")
    
    # Validate and adjust hours for each appliance
    validated_hours = {
        app: validate_hours(app, appliance_hours.get(app))
        for app in appliance_dict.keys()
        if appliance_dict[app] > 0
    }
    
    # Calculate total appliances for fuzzy logic
    total_appliances = sum(appliance_dict.values())
    
    # If no appliances are selected, return zero consumption
    if total_appliances == 0:
        return {
            'fuzzy_consumption': 0.0,
            'actual_consumption': 0.0,
            'appliance_consumptions': {},
            'appliance_hours': {}
        }
    
    # Calculate average usage hours for fuzzy logic
    total_usage = sum(hours * appliance_dict[app] 
                     for app, hours in validated_hours.items())
    avg_usage_hours = total_usage / total_appliances if total_appliances > 0 else 0
    
    if not (0 <= total_appliances <= 20):
        raise ValueError("Total number of appliances must be between 0 and 20")
    if not (0 <= season_val <= 2):
        raise ValueError("Season must be 0 (Winter), 1 (Monsoon), or 2 (Summer)")

    try:
        # Get fuzzy prediction
        sim = create_fuzzy_system()
        sim.input['appliances'] = float(total_appliances)
        sim.input['usage_hours'] = float(avg_usage_hours)
        sim.input['season'] = float(season_val)
        
        # Compute with error handling
        try:
            sim.compute()
            fuzzy_consumption = float(sim.output['consumption'])
        except Exception as e:
            # If fuzzy computation fails, fall back to actual consumption
            fuzzy_consumption = 0.0
        
        # Get actual consumption based on power ratings and individual hours
        actual_consumption = calculate_actual_consumption(appliance_dict, validated_hours)
        
        # Calculate individual appliance consumptions
        appliance_consumptions = {
            app: (count * APPLIANCE_DATA[app]['power'] * validated_hours[app] / 1000)
            for app, count in appliance_dict.items()
            if app in APPLIANCE_DATA and count > 0
        }
        
        # Return detailed consumption data
        return {
            'fuzzy_consumption': fuzzy_consumption,
            'actual_consumption': actual_consumption,
            'appliance_consumptions': appliance_consumptions,
            'appliance_hours': validated_hours
        }
        
    except Exception as e:
        # Log the specific error for debugging
        print(f"Debug - Error in prediction: {str(e)}")
        # Return fallback values
        return {
            'fuzzy_consumption': 0.0,
            'actual_consumption': calculate_actual_consumption(appliance_dict, validated_hours),
            'appliance_consumptions': {
                app: (count * APPLIANCE_DATA[app]['power'] * validated_hours[app] / 1000)
                for app, count in appliance_dict.items()
                if app in APPLIANCE_DATA and count > 0
            },
            'appliance_hours': validated_hours
        }

def safe_int(value, default=0):
    try:
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default

def safe_float(value, default=0.0):
    try:
        return float(value) if value is not None else default
    except (ValueError, TypeError):
        return default
