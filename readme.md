# E-Bill Estimation System

An intelligent electricity bill estimation system that uses fuzzy logic to predict electricity consumption and costs. Built with Python Flask and designed specifically for Indian households.

![Electricity Bill Estimator](https://raw.githubusercontent.com/hackerviper/e-bill-estimation/master/static/preview.png)

## 🌟 Features

- **Smart Appliance Management**
  - Support for 10+ common household appliances
  - Individual usage hour tracking
  - Pre-configured power ratings based on Indian appliances

- **Intelligent Estimation**
  - Fuzzy logic-based consumption prediction
  - Seasonal variation consideration (Winter/Monsoon/Summer)
  - Realistic power consumption calculations

- **Detailed Analysis**
  - Per-appliance consumption breakdown
  - Daily and monthly consumption estimates
  - Itemized cost calculation
  - Seasonal adjustments

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/hackerviper/e-bill-estimation.git
   cd e-bill-estimation
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # Linux/MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open http://localhost:5000 in your browser

## 💡 Supported Appliances

| Appliance | Power (Watts) | Default Hours |
|-----------|---------------|---------------|
| Fan | 75W | 8 hrs |
| LED Light | 40W | 6 hrs |
| Refrigerator | 150W | 24 hrs |
| AC (1.5 ton) | 1500W | 6 hrs |
| LED TV | 100W | 4 hrs |
| Washing Machine | 500W | 2 hrs |
| Microwave | 800W | 1 hr |
| Computer | 150W | 4 hrs |
| Water Heater | 2000W | 1 hr |
| Iron | 1000W | 1 hr |

## 🛠️ Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, TailwindCSS
- **AI**: scikit-fuzzy for Fuzzy Logic
- **Data Processing**: NumPy

## 📊 Screenshots

(Add screenshots here)

## 🤝 Contributing

Feel free to:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with focus on Indian household electricity consumption patterns
- Power ratings based on standard Indian market appliances
- Fuzzy logic implementation inspired by real-world usage patterns