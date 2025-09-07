# 🌧️ Australian Weather Prediction App

## 📋 Project Overview
A Streamlit web application that predicts whether it will rain tomorrow in Australia based on current weather conditions. Uses a trained Decision Tree model to provide accurate weather forecasts.

## 🎯 Objective
- Predict next-day rainfall using current weather parameters
- Provide user-friendly web interface for weather prediction
- Help users plan activities based on weather forecasts

## 📊 Dataset Features
The model uses the following weather parameters:
- **Max Temperature (°C)**: Maximum temperature for the day
- **Rainfall (mm)**: Amount of rainfall
- **Wind Gust Speed (km/h)**: Maximum wind speed
- **Humidity at 9 AM (%)**: Morning humidity levels
- **Humidity at 3 PM (%)**: Afternoon humidity levels
- **Pressure at 9 AM (hPa)**: Morning atmospheric pressure
- **Pressure at 3 PM (hPa)**: Afternoon atmospheric pressure
- **Temperature at 3 PM (°C)**: Afternoon temperature
- **Rain Today**: Whether it rained today (Yes/No)
- **RISK_MM**: Risk of rainfall amount

## 🛠️ Technologies Used
- **Python 3.x**
- **Streamlit** - Web application framework
- **Joblib** - Model serialization
- **NumPy** - Numerical computations
- **Scikit-learn** - Machine learning (Decision Tree)

## 🤖 Model Details
- **Algorithm**: Decision Tree Classifier
- **Target**: Rain Tomorrow (Yes/No)
- **Preprocessing**: Label encoding for categorical variables
- **Model Files**: 
  - `DecisionTreeClassifier.joblib` - Trained model
  - `RainToday_label_encoder.joblib` - Label encoder for categorical data

## 🚀 How to Run
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure model files are in the project directory:
   - `DecisionTreeClassifier.joblib`
   - `RainToday_label_encoder.joblib`
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser to `http://localhost:8501`

## 📱 App Features
- **Interactive Input Form**: Enter weather parameters
- **Real-time Prediction**: Get instant rain forecast
- **User-friendly Interface**: Clean and intuitive design
- **Weather Parameter Validation**: Reasonable default values

## 📁 Project Structure
```
Weather_AUS_Machine_learning/
├── app.py                              # Main Streamlit application
├── DecisionTreeClassifier.joblib       # Trained model
├── RainToday_label_encoder.joblib      # Label encoder
├── Decision Tree.pkl                   # Alternative model format
├── RainToday_label_encoder.pkl         # Alternative encoder format
├── README.md                          # Project documentation
└── requirements.txt                   # Dependencies
```

## 🔮 Future Enhancements
- Model performance metrics display
- Historical weather data visualization
- Multiple location support
- Weather trend analysis
- Model comparison dashboard

## 👨‍💻 Author
Machine Learning Project

---
⭐ If you find this project helpful, please give it a star!
