# Electricity Usage & Bill Estimator

A sophisticated web application that estimates electricity consumption and costs using fuzzy logic and real-world appliance power ratings. This tool is specifically designed for Indian households, with a focus on providing accurate estimates for tier 3 city homes.

## Features

- **Comprehensive Appliance Management**
  - Support for common household appliances (fans, lights, AC, TV, fridge)
  - Additional miscellaneous appliances (washing machine, microwave, computer, etc.)
  - Individual usage hours tracking for each appliance
  - Pre-configured power ratings based on typical Indian appliances

- **Smart Estimation System**
  - Fuzzy logic-based consumption prediction
  - Seasonal variation consideration (Winter, Monsoon, Summer)
  - Realistic power consumption calculation based on actual appliance ratings
  - Automatic validation of usage patterns

- **Detailed Analysis**
  - Per-appliance consumption breakdown
  - Daily and monthly consumption estimates
  - Itemized cost calculation
  - Season-specific adjustments

## Technical Details

### Power Ratings (Watts)
- Fan: 75W
- LED Light: 40W
- Refrigerator: 150W
- AC (1.5 ton): 1500W
- LED TV: 100W
- Washing Machine: 500W
- Microwave: 800W
- Computer: 150W
- Water Heater: 2000W
- Iron: 1000W

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd electricity_fuzzy_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirement.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter your appliance details:
   - Specify the number of each type of appliance
   - Set daily usage hours for each appliance
   - Select the current season
   - Enter your electricity cost per unit (₹)

4. Click "Calculate Consumption" to see the detailed analysis

## Deployment on PythonAnywhere

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com)

2. Upload your files:
   - Go to the Files tab
   - Create a new directory: `electricity_fuzzy_project`
   - Upload all project files to this directory
   - Or use Git to clone your repository:
     ```bash
     git clone https://github.com/your-username/electricity_fuzzy_project.git
     ```

3. Set up a virtual environment:
   - Open a Bash console from PythonAnywhere
   - Navigate to your project directory
   ```bash
   cd electricity_fuzzy_project
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirement.txt
   ```

4. Configure the Web App:
   - Go to the Web tab
   - Click "Add a new web app"
   - Choose "Manual Configuration"
   - Select Python 3.11
   - Set the following configurations:
     - Source code: `/home/YOUR_USERNAME/electricity_fuzzy_project`
     - Working directory: `/home/YOUR_USERNAME/electricity_fuzzy_project`
     - WSGI configuration file: Use the provided `wsgi.py`
     - Virtual environment: `/home/YOUR_USERNAME/electricity_fuzzy_project/venv`

5. Update WSGI Configuration:
   - In the Web tab, click on the WSGI configuration file link
   - Replace the content with the provided `wsgi.py` content
   - Update `YOUR_USERNAME` with your PythonAnywhere username
   - Click Save

6. Configure Static Files:
   - In the Web tab, add these static file mappings:
   ```
   URL: /static/
   Directory: /home/YOUR_USERNAME/electricity_fuzzy_project/static
   ```

7. Reload the web app:
   - Click the Reload button in the Web tab
   - Your app will be available at: `http://YOUR_USERNAME.pythonanywhere.com`

Note: Replace `YOUR_USERNAME` with your actual PythonAnywhere username in all paths.

## Technical Architecture

### Frontend
- HTML5 with Tailwind CSS for styling
- Responsive design suitable for all device sizes
- JavaScript for dynamic form handling
- No-cache implementation for accurate results

### Backend
- Flask web framework
- scikit-fuzzy for fuzzy logic implementation
- NumPy for numerical computations
- Custom validation and calculation modules

### Fuzzy Logic System
- Input variables:
  - Number of appliances (0-20)
  - Usage hours (0-24)
  - Season (Winter/Monsoon/Summer)
- Output:
  - Daily consumption (kWh)
  - Fuzzy sets: very_low, low, medium, high, very_high
  - Realistic consumption ranges for tier 3 city context

## Limitations
- Maximum 20 appliances total
- Usage hours must be within realistic ranges for each appliance
- Calculations are estimates based on average power consumption
- Seasonal variations are simplified into three categories

## Dependencies
- Flask==3.0.0
- scikit-fuzzy==0.4.2
- numpy==1.24.3
- Additional dependencies listed in `requirement.txt`

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Developed with focus on Indian household electricity consumption patterns
- Power ratings based on standard Indian market appliances
- Fuzzy logic implementation inspired by real-world usage patterns