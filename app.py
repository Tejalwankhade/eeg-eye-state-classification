import streamlit as st
import numpy as np
import pickle
import bz2

st.set_page_config(page_title="EEG Eye State Detection")

st.title("👁️ EEG Eye State Detection App")
st.write("Predicts whether eyes are OPEN or CLOSED using EEG signals.")

# --------------------------
# Load compressed bz2 model
# --------------------------
with bz2.BZ2File("Eye_State_model.pbz2", "rb") as f:
    model = pickle.load(f)

st.subheader("Enter EEG Feature Values")

feature_names = [
    "AF3","F7","F3","FC5","T7","P7",
    "O1","O2","P8","T8","FC6","F4","F8","AF4"
]

inputs = []

for name in feature_names:
    value = st.number_input(name, value=4300.0)
    inputs.append(value)

if st.button("Predict Eye State"):
    data = np.array(inputs).reshape(1, -1)

    # model may be pipeline or raw RF — both will work
    pred = model.predict(data)[0]

    if pred == 0:
        st.success("🟢 Eye State: OPEN")
    else:
        st.error("🔴 Eye State: CLOSED")
