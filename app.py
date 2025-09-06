import streamlit as st
import joblib
import pandas as pd

# --- Eğitilmiş modeli yükle ---
model = joblib.load("model.pkl")

st.set_page_config(page_title="Music Therapy Effectiveness Predictor in Tinnitus", layout="centered")
st.title("🎶 Music Therapy Effectiveness Predictor in Tinnitus")

st.write("Enter the following values to predict therapy benefit:")

# --- Inputs ---
thi = st.number_input("Tinnitus Handicap Inventory (THI)", min_value=0, max_value=100, step=1)
bdi = st.number_input("Beck Depression Inventory (BDI)", min_value=0, max_value=63, step=1)
vas = st.number_input("VAS - Discomfort Level (0-10)", min_value=0, max_value=10, step=1)

# Residual Inhibition: 0 = None, 1 = Partial, 2 = Complete
residual_inhibition = st.selectbox(
    "Residual Inhibition",
    options=[0, 1, 2],
    format_func=lambda x: "No (0)" if x == 0 else ("Partial (1)" if x == 1 else "Complete (2)")
)

# --- Prediction ---
if st.button("Predict"):
    X_new = pd.DataFrame([{
        "THI": thi,
        "BDI": bdi,
        "VAS": vas,
        "Residual Inhibition": residual_inhibition
    }])
    prediction = model.predict(X_new)[0]

    if prediction == 0:
        st.error("❌ Music therapy is **not recommended**")
    else:
        st.success("🎵 Music therapy is **recommended**")
