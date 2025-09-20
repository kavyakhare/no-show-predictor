<h1 align="center">🩺 <b>Smart Healthcare: No-Show Prediction</b></h1>
This project predicts whether a patient will miss their scheduled medical appointment based on demographic and appointment-related factors.
It uses Machine Learning and is deployed as an interactive Streamlit web app.

## 📊 **Project Overview**
Hospitals and clinics lose significant time and resources due to patients not showing up for appointments.
This project leverages historical appointment data to build a predictive model that estimates the probability of a patient missing their appointment.

Users can enter appointment details into the app and instantly receive a prediction.

## 🚀 **Features**
-Predict if a patient will show up or miss the appointment.
-Shows probability of no-show (e.g., “70% chance of missing”).
-Simple, interactive web interface built with Streamlit.
-Model trained using Random Forest and Logistic Regression, chosen by best F1 score.

## 🔗 **Live Demo**
[Click here to use the app](https://no-show-predictor.streamlit.app/)

## 🧠 **Dataset**
This app is based on the Medical Appointment No Shows dataset from Kaggle

## 🏗️ **Model Training**
1.Data cleaned & preprocessed (dates, categorical variables, etc.).
2.Trained Logistic Regression and Random Forest models.
3.Compared models using F1 Score.
4.Saved best model using joblib:

## 🌐 **Deployment**
The app is deployed on Streamlit Cloud.

## 🖥️ **How to Use**
-Open the web app.
-Enter patient and appointment details into the form.
-Click Predict.
-The app shows whether the patient is likely to show up or not, and the probability of no-show.

## 📊 **Tech Stack**

Python

scikit-learn

pandas, numpy

joblib

Streamlit (for deployment)

📷 Screenshots

📄 License

This project is licensed under the MIT License.
