
import streamlit as st

def calculate_body_fat(density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist):
    # Jackson-Pollock 7-site skinfold formula for males
    suprailiac = abdomen  # Correcting the missing variable
    sum_skinfolds = chest + abdomen + thigh + suprailiac + knee + biceps + forearm
    body_fat_percentage = 495 / (1.097 - 0.000422 * sum_skinfolds + 0.000000153 * (sum_skinfolds ** 2) - 0.00000053 * age)
    return body_fat_percentage

def main():
    st.title("Body Fat Percentage Calculator")

    st.sidebar.header("User Input")
    density = st.sidebar.number_input("Density", min_value=0.0, max_value=3.0, value=1.0)
    age = st.sidebar.number_input("Age", min_value=1, max_value=150, value=25)
    weight = st.sidebar.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0)
    height = st.sidebar.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=175.0)
    neck = st.sidebar.number_input("Neck (cm)", min_value=1.0, max_value=50.0, value=35.0)
    chest = st.sidebar.number_input("Chest (cm)", min_value=1.0, max_value=200.0, value=90.0)
    abdomen = st.sidebar.number_input("Abdomen (cm)", min_value=1.0, max_value=200.0, value=80.0)
    hip = st.sidebar.number_input("Hip (cm)", min_value=1.0, max_value=200.0, value=95.0)
    thigh = st.sidebar.number_input("Thigh (cm)", min_value=1.0, max_value=200.0, value=55.0)
    knee = st.sidebar.number_input("Knee (cm)", min_value=1.0, max_value=200.0, value=40.0)
    ankle = st.sidebar.number_input("Ankle (cm)", min_value=1.0, max_value=200.0, value=25.0)
    biceps = st.sidebar.number_input("Biceps (cm)", min_value=1.0, max_value=100.0, value=30.0)
    forearm = st.sidebar.number_input("Forearm (cm)", min_value=1.0, max_value=100.0, value=25.0)
    wrist = st.sidebar.number_input("Wrist (cm)", min_value=1.0, max_value=50.0, value=17.0)

    if st.sidebar.button("Calculate Body Fat Percentage"):
        body_fat_percentage = calculate_body_fat(density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist)
        st.success(f"Estimated Body Fat Percentage: {body_fat_percentage:.2f}%")

if __name__ == "__main__":
    main()
