import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

st.title("❤️ Heart Disease Prediction")

# Inputs
age = st.number_input("Age", 1, 100)
sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
cp = st.number_input("Chest Pain Type (0-3)", 0, 3)
trestbps = st.number_input("Resting BP", 80, 200)
chol = st.number_input("Cholesterol", 100, 400)
fbs = st.selectbox("Fasting Blood Sugar >120 (1=True,0=False)", [1, 0])
restecg = st.number_input("Rest ECG (0-2)", 0, 2)
thalach = st.number_input("Max Heart Rate", 60, 220)
exang = st.selectbox("Exercise Angina (1=Yes,0=No)", [1, 0])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
slope = st.number_input("Slope (0-2)", 0, 2)
ca = st.number_input("CA (0-3)", 0, 3)
thal = st.number_input("Thal (1-3)", 1, 3)

# Prediction
if st.button("Predict"):
    data = np.array([[age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]])

    data = scaler.transform(data)
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk")