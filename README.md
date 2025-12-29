# eeg-eye-state-classification
# 👁️ EEG Eye State Classification (Random Forest + Streamlit)

This project predicts **eye state (Open/Closed)** using **EEG brain signal data**.  
A **Random Forest classifier** is trained on EEG electrode signals and deployed as a **Streamlit web app**.

---

## 🚀 Live Demo

Try the app here:

🔗 **https://eeg-eye-state-classification-afpjkoczeyxwbz5zgskyzs.streamlit.app/**

---

## 🧠 Problem Statement

Given EEG signals from electrodes placed on the scalp, classify whether:

- `0` → Eyes Open  
- `1` → Eyes Closed  

The model uses 14 EEG channel values:

`AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4`

---

## 🛠️ Tech Stack

- Python
- Scikit-Learn
- Random Forest Classifier
- Streamlit
- NumPy / Pandas
- Pickle (compressed with bz2)

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `app.py` | Streamlit web app |
| `Eye_State_model.pbz2` | Trained Random Forest model (compressed pickle) |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🧩 Model Details

- Random Forest Classifier
- Trained on EEG features
- Pipeline includes preprocessing
- Saved as **compressed pickle** (`bz2`)

Model created using:

```python
with bz2.BZ2File("Eye_State_model.pbz2", "wb") as f:
    pickle.dump(rf, f)

How to Use the App

Enter EEG feature values manually

Click Predict

Output will show:

🟢 Eye Open

🔴 Eye Closed
