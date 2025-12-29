import streamlit as st
import numpy as np
import pandas as pd
import pickle

# --------------------
# Load saved model
# --------------------
with open("Eye_State_rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("EEG Eye State Detection App 👁️")
st.write("Random Forest model to classify eye state using EEG signals.")

st.markdown("### Enter EEG Signal Features")

# EEG input fields
AF3 = st.number_input("AF3", value=4300.0)
F7 = st.number_input("F7", value=4000.0)
F3 = st.number_input("F3", value=4200.0)
FC5 = st.number_input("FC5", value=4150.0)
T7 = st.number_input("T7", value=4350.0)
P7 = st.number_input("P7", value=4580.0)
O1 = st.number_input("O1", value=4100.0)
O2 = st.number_input("O2", value=4630.0)
P8 = st.number_input("P8", value=4210.0)
T8 = st.number_input("T8", value=4230.0)
FC6 = st.number_input("FC6", value=4210.0)
F4 = st.number_input("F4", value=4280.0)
F8 = st.number_input("F8", value=4630.0)
AF4 = st.number_input("AF4", value=4390.0)

# Put inputs into correct order
input_features = np.array([[AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4]])

if st.button("Predict Eye State"):
    prediction = model.predict(input_features)[0]

    if prediction == 0:
        st.success("🟢 Eye State: OPEN")
    else:
        st.error("🔴 Eye State: CLOSED")
