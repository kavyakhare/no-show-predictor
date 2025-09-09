import model_training
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Healthcare No-Show Predictor", page_icon="🩺", layout="centered")
st.title("🩺 Smart Healthcare: No-Show Prediction")
st.caption("Enter appointment details to estimate the chance a patient will miss their appointment.")

# ---------- Load artifacts (cached) ----------
@st.cache_resource
def load_model():
    return joblib.load("no_show_model.joblib")

@st.cache_resource
def load_neighbourhoods():
    try:
        return joblib.load("neighbourhoods.joblib")
    except Exception:
        # Fallback if file missing
        return ["JARDIM CAMBURI", "JARDIM DA PENHA"]

model = load_model()
neighbourhoods = load_neighbourhoods()

# Keep options consistent with training
day_options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
gender_options = ["F","M"]

with st.form("prediction_form"):
    st.subheader("Enter Details")

    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", gender_options, index=0)
        age = st.number_input("Age", min_value=0, max_value=120, value=35, step=1)
        scholarship = st.selectbox("Scholarship (0/1)", [0,1], index=0)
        hypertension = st.selectbox("Hypertension (0/1)", [0,1], index=0)
        diabetes = st.selectbox("Diabetes (0/1)", [0,1], index=0)
    with col2:
        alcoholism = st.selectbox("Alcoholism (0/1)", [0,1], index=0)
        handicap = st.selectbox("Handicap (0/1)", [0,1], index=0)
        sms_received = st.selectbox("SMS_received (0/1)", [0,1], index=0)
        waiting_days = st.number_input("Waiting Days", min_value=0, max_value=365, value=5, step=1)
        appointment_month = st.number_input("Appointment Month (1-12)", min_value=1, max_value=12, value=5, step=1)

    neighbourhood = st.selectbox("Neighbourhood", neighbourhoods, index=0)
    day_of_week = st.selectbox("Day of Week", day_options, index=0)

    show_row = st.checkbox("Show input row (debug)", value=False)
    submit = st.form_submit_button("Predict")

if submit:
    # Build a one-row DataFrame exactly like training columns
    row = pd.DataFrame([{
        "Gender": gender,
        "Neighbourhood": neighbourhood,
        "DayOfWeek": day_of_week,
        "Age": age,
        "Scholarship": scholarship,
        "Hypertension": hypertension,
        "Diabetes": diabetes,
        "Alcoholism": alcoholism,
        "Handicap": handicap,
        "SMS_received": sms_received,
        "waiting_days": waiting_days,
        "AppointmentMonth": appointment_month
    }])

    # Enforce column order (extra safety)
    cols = ['Gender','Neighbourhood','DayOfWeek','Age','Scholarship',
            'Hypertension','Diabetes','Alcoholism','Handicap',
            'SMS_received','waiting_days','AppointmentMonth']
    row = row[cols]

    if show_row:
        st.write("Input row:", row)

    # Predict with protection
    try:
        pred = model.predict(row)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(row)[0][1])  # prob of No-Show (class 1)

        if pred == 1:
            st.error("Prediction: **No-Show** 🟥" + (f"  (prob ≈ {proba:.2f})" if proba is not None else ""))
        else:
            # If pred==0, prob shown is probability of show (1 - no-show prob)
            st.success("Prediction: **Will Show** 🟩" + (f"  (prob ≈ {(1-proba):.2f})" if proba is not None else ""))

    except Exception as e:
        st.error(f"Something went wrong during prediction: {e}")

st.markdown("---")
st.caption("Model: scikit-learn pipeline (OneHot + Logistic/RandomForest). This is a demo; not medical advice.")
