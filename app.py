from flask import Flask, render_template, request, make_response
from fuzzy_logic import predict_consumption, safe_int, safe_float, APPLIANCE_DATA
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        response = make_response(render_template('index.html', result=None, appliance_data=APPLIANCE_DATA))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
        
    if request.method == 'POST':
        try:
            # Get base appliance counts
            appliances = {
                'fan': safe_int(request.form.get('fan', 0)),
                'light': safe_int(request.form.get('light', 0)),
                'fridge': safe_int(request.form.get('fridge', 0)),
                'ac': safe_int(request.form.get('ac', 0)),
                'tv': safe_int(request.form.get('tv', 0)),
                'washing_machine': safe_int(request.form.get('washing_machine', 0)),
                'microwave': safe_int(request.form.get('microwave', 0)),
                'computer': safe_int(request.form.get('computer', 0)),
                'water_heater': safe_int(request.form.get('water_heater', 0)),
                'iron': safe_int(request.form.get('iron', 0))
            }

            # Get individual appliance hours
            appliance_hours = {
                app: safe_float(request.form.get(f'{app}_hours'))
                for app in appliances.keys()
                if appliances[app] > 0
            }

            season = safe_int(request.form.get('season', 0))
            unit_cost = safe_float(request.form.get('unit_cost', 0.0))

            # Input validation
            total_appliances = sum(appliances.values())
            if total_appliances > 20:
                raise ValueError("Total number of appliances cannot exceed 20")
            if unit_cost <= 0:
                raise ValueError("Unit cost must be greater than 0")

            # Calculate consumption using enhanced prediction
            consumption_data = predict_consumption(appliances, appliance_hours, season)
            
            # Calculate costs
            daily_consumption = consumption_data['actual_consumption']
            monthly_consumption = daily_consumption * 30
            monthly_bill = round(monthly_consumption * unit_cost, 2)

            # Format appliance consumptions for display
            appliance_details = []
            for app, consumption in consumption_data['appliance_consumptions'].items():
                if appliances[app] > 0:
                    daily_cost = consumption * unit_cost
                    monthly_cost = daily_cost * 30
                    appliance_details.append({
                        'name': app.replace('_', ' ').title(),
                        'count': appliances[app],
                        'power': APPLIANCE_DATA[app]['power'],
                        'hours': consumption_data['appliance_hours'][app],
                        'daily_consumption': round(consumption, 2),
                        'daily_cost': round(daily_cost, 2),
                        'monthly_cost': round(monthly_cost, 2)
                    })

            result = {
                'daily_consumption': round(daily_consumption, 2),
                'monthly_consumption': round(monthly_consumption, 2),
                'monthly_bill': monthly_bill,
                'appliance_count': total_appliances,
                'season_text': ['Winter', 'Monsoon', 'Summer'][season],
                'appliance_details': appliance_details,
                'unit_cost': unit_cost
            }

            response = make_response(render_template('index.html', 
                                                   result=result, 
                                                   appliance_data=APPLIANCE_DATA))
            response.headers['Cache-Control'] = 'no-store'
            response.headers['Pragma'] = 'no-cache'
            return response

        except ValueError as e:
            result = {'error': str(e)}
        except Exception as e:
            result = {'error': f"An unexpected error occurred: {str(e)}"}

        return render_template('index.html', result=result, appliance_data=APPLIANCE_DATA)

if __name__ == '__main__':
    # Only use debug mode when running locally
    is_production = os.environ.get('FLASK_ENV') == 'production'
    app.run(debug=not is_production)
