import streamlit as st
import tensorflow as tf

# Replace 'path/to/your/model.h5' with the actual path to your model
model = tf.keras.models.load_model('churn.hdf5')

# ... use the model for prediction


# Model details (customize based on your model)
MODEL_INPUT_FEATURES = [
    "credit_score", "geography", "gender", "age", "tenure", "balance",
    "num_of_products", "has_cr_card", "is_active_member", "estimated_salary"
]
MODEL_OUTPUT_FEATURE = "churn_probability"  # Or "churn_label" if binary

# App title and header
st.title("Customer Churn Prediction App")
st.subheader("Using an Artificial Neural Network Model")

# User input form
user_input = {}
for feature in MODEL_INPUT_FEATURES:
    if feature == "credit_score":
        user_input[feature] = st.slider(feature.title(), 300, 850, 600)
    elif feature == "geography":
        user_input[feature] = st.selectbox(feature.title(), ["France","Germany","Spain"])
    elif feature == "gender":
        user_input[feature] = st.radio(feature.title(), ["Male", "Female"])
    elif feature == "age":
        user_input[feature] = st.number_input(feature.title(), min_value=18)
    elif feature == "tenure":
        user_input[feature] = st.number_input(feature.title(), min_value=0)
    elif feature == "balance":
        user_input[feature] = st.number_input(feature.title(), min_value=0)
    elif feature == "num_of_products":
        user_input[feature] = st.number_input(feature.title(), min_value=0)
    elif feature == "has_cr_card":
        user_input[feature] = st.checkbox(feature.title())
    elif feature == "is_active_member":
        user_input[feature] = st.checkbox(feature.title())
    elif feature == "estimated_salary":
        user_input[feature] = st.number_input(feature.title(), min_value=0)

# Prediction function
def predict_churn(user_input):
    # Preprocess data if needed (e.g., one-hot encode categorical features)
    # ... (Ensure preprocessing matches your model's requirements)

    # Make prediction using your model
    prediction = your_model.predict(user_input[MODEL_INPUT_FEATURES])

    return prediction[0][MODEL_OUTPUT_FEATURE]

# Predict button and result display
if st.button("Predict Churn"):
    prediction = predict_churn(user_input)
    if prediction >= 0.5:  # Adjust threshold as needed based on model
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is unlikely to churn.")
    st.write(f"Churn probability: {prediction:.2f}")

# Additional insights or visualizations (optional)
# ... (Consider adding charts or explanations based on model outputs)


# ...

