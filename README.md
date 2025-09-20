🩺 Smart Healthcare: No-Show Prediction

This project predicts whether a patient will miss their scheduled medical appointment based on demographic and appointment-related factors.
It uses Machine Learning and is deployed as an interactive Streamlit web app.

📖 Overview

Hospitals and clinics lose significant time and resources due to patients not showing up for appointments.
This project leverages historical appointment data to build a predictive model that estimates the probability of a patient missing their appointment.

Users can enter appointment details into the app and instantly receive a prediction.

⚙️ Features

Predict if a patient will show up or miss the appointment.

Shows probability of no-show (e.g., “70% chance of missing”).

Simple, interactive web interface built with Streamlit.

Model trained using Random Forest and Logistic Regression, chosen by best F1 score.

🧠 Dataset

This app is based on the Medical Appointment No Shows dataset from Kaggle
.

Key columns used:

Column	Description
PatientId	Patient identifier
AppointmentID	Appointment identifier
Gender	Male/Female
ScheduledDay	Date when the appointment was scheduled
AppointmentDay	Date of the appointment
Age	Age of the patient
Neighbourhood	Location of the hospital
Scholarship	1 if enrolled in welfare program, else 0
Hypertension	1 if present, else 0
Diabetes	1 if present, else 0
Alcoholism	1 if present, else 0
Handcap	1 if present, else 0
SMS_received	1 if SMS reminder received, else 0
No-show	Target variable (Yes = missed, No = attended)
🏗️ Model Training

Data cleaned & preprocessed (dates, categorical variables, etc.).

Trained Logistic Regression and Random Forest models.

Compared models using F1 Score.

Saved best model using joblib:

joblib.dump(best_model, "no_show_model.joblib")

🌐 Deployment

The app is deployed on Streamlit Cloud.

Local Setup:
# Clone repo
git clone https://github.com/yourusername/no-show-predictor.git
cd no-show-predictor

# Install requirements
pip install -r requirements.txt

# Run locally
streamlit run app.py

Live App:

🔗 Click here to try the app

🖥️ How to Use

Open the web app.

Enter patient and appointment details into the form.

Click Predict.

The app shows whether the patient is likely to show up or not, and the probability of no-show.

📊 Tech Stack

Python

scikit-learn

pandas, numpy

joblib

Streamlit (for deployment)

📷 Screenshots

📄 License

This project is licensed under the MIT License.
