import streamlit as st
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("coffee_model.keras")

st.title("Coffee Roast Predictor")

st.write("Predict whether a coffee roast is GOOD or BAD.")

temperature = st.slider(
    "Roasting Temperature (°C)",
    150,
    300,
    220
)

time = st.slider(
    "Roasting Time (minutes)",
    5,
    30,
    15
)

if st.button("Predict"):

    prediction = model.predict(
        np.array([[temperature, time]]),
        verbose=0
    )

    probability = prediction[0][0]

    

    if probability >= 0.5:
        st.write(f"Confidence: {probability*100:.2f}%")
        st.success("GOOD ROAST")
    else:
        st.write(f"Confidence: {(1-probability)*100:.2f}%")
        st.error("BAD ROAST")