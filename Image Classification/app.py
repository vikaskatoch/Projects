
import streamlit as st
import tensorflow as tf
import cv2
import numpy as np


model = tf.keras.models.load_model('CNNImageClassification.hdf5')

def classify_image(image_bytes):
    """Classifies an image using the loaded CNN model.

    Args:
        image_bytes (bytes): Raw image data read from the uploaded file.

    Returns:
        tuple: A tuple containing the predicted class label (string) and probability (float).
    """

    # Decoding image bytes and convert to NumPy array
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    # Preprocessing image
    image = cv2.resize(image, (100, 100))  # Assuming your model's input size
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)[0]
    class_names = ['Cat', 'Dog']  # Assuming your model outputs these labels

    return class_names[np.argmax(prediction)], prediction[np.argmax(prediction)]

# Creating streamlit app
st.title("Cat vs. Dog Image Classifier")
st.subheader("Using a Convolutional Neural Network")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])

if uploaded_file is not None:
    image_bytes = uploaded_file.read()

    prediction, probability = classify_image(image_bytes)

    # Displaying image and prediction
    st.image(image_bytes)
    st.write(f"Predicted: {prediction} with {probability:.2f} confidence")

