# Smart Electricity Bill Calculator

A simple and smart tool that helps Indian families estimate their monthly electricity bills accurately. It looks at your appliance usage and tells you how much electricity you might use and what your bill could be.

## 🌟 Key Features

### 1. Easy to Use
- Just tell us which appliances you have (like fans, TV, fridge)
- Enter how many hours you use them
- Select your season (Summer/Winter/Monsoon)
- Get your bill estimate instantly!

### 2. Smart Calculations
- Uses advanced technology (fuzzy logic) to think like experts
- Considers seasonal changes in usage
- Gives realistic estimates based on Indian homes
- Shows cost for each appliance separately

### 3. Accurate Power Ratings
- Pre-loaded with common Indian appliance power ratings
- Realistic usage patterns
- Based on typical Indian household needs

## 📱 How to Use

### Step 1: Setting Up
1. Make sure you have Python installed (version 3.11.0 or newer)
2. Open command prompt (cmd) and type these commands:
   ```bash
   # Download the project
   git clone https://github.com/hackerviper/e-bill-estimation.git
   cd e-bill-estimation

   # Set up Python
   python -m venv venv

   # For Windows users, type:
   .\venv\Scripts\activate

   # For Linux/Mac users, type:
   source venv/bin/activate

   # Install required packages
   pip install -r requirement.txt

   # Start the calculator
   python app.py
   ```
3. Open your web browser and go to: http://localhost:5000

### Step 2: Using the Calculator
1. Add your appliances:
   - Enter how many fans, lights, AC etc. you have
   - Set daily usage hours for each
2. Select your current season
3. Enter electricity rate (₹/unit) from your area
4. Click "Calculate" to see your estimate

## 💡 Supported Appliances

Here are the common appliances we support with their typical power usage:

| Appliance | Power | Normal Daily Use |
|-----------|-------|-----------------|
| Fan | 75W | 8 hours |
| LED Light | 40W | 6 hours |
| Fridge | 150W | 24 hours |
| AC (1.5 ton) | 1500W | 6 hours |
| LED TV | 100W | 4 hours |
| Washing Machine | 500W | 2 hours |
| Microwave | 800W | 1 hour |
| Computer | 150W | 4 hours |
| Geyser | 2000W | 1 hour |
| Iron | 1000W | 1 hour |

## 🔧 Technology Used
- Website: Python Flask
- Design: HTML5 & TailwindCSS
- Smart Calculations: Fuzzy Logic
- Data Handling: NumPy

## 🤝 Want to Help?
We welcome improvements! Here's how you can help:
1. Fork the project
2. Make your changes
3. Send us your improvements through Pull Request

## 📞 Need Help?
If you have questions or suggestions:
1. Create an issue on GitHub
2. Email us at: [-]
3. Connect on LinkedIn: [-]

## 📜 License
This project uses MIT License - see the LICENSE file for details.

## 🙏 Special Thanks
- Made specially for Indian households
- Power ratings based on Indian market appliances
- Usage patterns from real Indian families

---
💡 **Tip**: For most accurate results, check your appliance's actual power rating from its label or manual.

Made with ❤️ for Indian homes
