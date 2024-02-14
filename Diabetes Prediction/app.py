import streamlit as st
import joblib
import numpy as np

# Load the saved model using joblib
model = joblib.load("logistic_regression_model.joblib")

st.title("Diabetes Prediction App")

# Collect user input for all eight features
feature1 = st.slider("Pregnancies", 0.0, 17.0)
feature2 = st.slider("Glucose", 0.0, 199.0)
feature3 = st.slider("BloodPressure", 0.0, 122.0)
feature4 = st.slider("SkinThickness", 0.0, 99.0)
feature5 = st.slider("Insulin", 0.0, 846.0)
feature6 = st.slider("BMI", 0.0, 67.0)
feature7 = st.slider("DiabetesPedigreeFunction", 0.0, 2.42)
feature8 = st.slider("Age", 0.0, 81.0)


# Create an array with all eight features
input_data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]])

# Make a prediction
prediction = model.predict(input_data)

st.write(f"Prediction: {int(prediction[0])}")

