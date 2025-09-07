import streamlit as st
import joblib

import numpy as np

with open("RainToday_label_encoder.joblib", "rb") as f:
    rain_encoder = joblib.load(f)
    
# # Load model and label encoder
# with open("DecisionTreeClassifier.joblib", "rb") as f:
#     model = joblib.load(f)



# Define feature input form
st.title("🌧️ Rain Tomorrow Prediction App")

st.markdown("Enter the weather parameters:")

max_temp = st.number_input("Max Temperature (°C)", value=25.0)
rainfall = st.number_input("Rainfall (mm)", value=0.0)
wind_gust_speed = st.number_input("Wind Gust Speed (km/h)", value=35.0)
humidity_9am = st.number_input("Humidity at 9 AM (%)", value=70.0)
humidity_3pm = st.number_input("Humidity at 3 PM (%)", value=50.0)
pressure_9am = st.number_input("Pressure at 9 AM (hPa)", value=1010.0)
pressure_3pm = st.number_input("Pressure at 3 PM (hPa)", value=1008.0)
temp_3pm = st.number_input("Temperature at 3 PM (°C)", value=22.0)
rain_today = st.selectbox("Did it rain today?", options=rain_encoder.classes_)
risk_mm = st.number_input("RISK_MM (Rainfall in next day)", value=0.0)

# Prediction button
if st.button("Predict"):
    # Encode RainToday
    rain_today_encoded = rain_encoder.transform([rain_today])[0]

    # Create input array
    input_data = np.array([[max_temp, rainfall, wind_gust_speed,
                            humidity_9am, humidity_3pm, pressure_9am,
                            pressure_3pm, temp_3pm, rain_today_encoded,
                            risk_mm]])

    # Predict
    
    prediction = model.predict(input_data)[0]

    # Show result
    st.success(f"🌤️ Prediction: {'Rain Tomorrow' if prediction == 1 else 'No Rain Tomorrow'}")
