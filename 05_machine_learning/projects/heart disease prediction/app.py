import streamlit as st
import pandas as pd
import joblib as jl


model = jl.load('SVM_heart.pkl')
scaler = jl.load('scaler.pkl')
expected_columns = jl.load('columns.pkl')

# expected_columns = [
#     'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
#     'Sex_M', 'ChestPainType_ASY', 'ChestPainType_ATA',
#     'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_LVH',
#     'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_N',
#     'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up'
# ]


st.title("❤️🦟 Heart Disease Prediction")
st.subheader("Developed by: M. Rayyan Shehzad")

st.markdown("Provide the following details...")


# Using feature of Main Unprocessed Data & Make sure the data types are correct and match the unprocessed data types
age = st.slider('Age', 18, 100, 40)
sex = st.selectbox('Gender', ['Male', 'Female'])
# chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'ASY', 'TA'])
# resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 80,200,120)
# cholesterol = st.number_input('Cholesterol (mg/dl)', 100, 600, 200)
# fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [1, 0]) 
# resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
# max_heart_rate = st.slider('Max Heart Rate' , 60, 220, 120)
# exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'])
# oldpeak = st.slider('Oldpeak (ST depression)', 0.0, 10.0, 1.0)
# st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'ASY', 'TA'], help="Type of chest pain experienced. ATA = Atypical Angina (chest pain not typical of heart-related pain), NAP = Non-Anginal Pain (pain likely unrelated to the heart), ASY = Asymptomatic (no chest pain at all, which can still indicate heart disease), TA = Typical Angina (classic chest pain caused by reduced blood flow to the heart)")
resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 80,200,120, help="Blood pressure measured while at rest, in millimeters of mercury (mm Hg). This is the systolic (top) number. Normal resting blood pressure is generally around 120 mm Hg; consistently high values (over 130-140) increase heart disease risk")
cholesterol = st.number_input('Cholesterol (mg/dl)', 100, 600, 200, help="Total cholesterol level in the blood, measured in milligrams per deciliter (mg/dl). A healthy level is generally below 200 mg/dl. High cholesterol can lead to blocked arteries and increased risk of heart disease")
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [1, 0], help="Indicates whether fasting blood sugar (measured after not eating for at least 8 hours) is above 120 mg/dl. 1 = Yes (elevated, may indicate diabetes or prediabetes), 0 = No (normal range). High fasting blood sugar is a risk factor for heart disease") 
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'], help="Results of the resting electrocardiogram (ECG/EKG), a test that records the heart's electrical activity. Normal = no abnormalities detected, ST = ST-T wave abnormality (may suggest reduced blood flow to the heart), LVH = Left Ventricular Hypertrophy (thickening of the heart's main pumping chamber, often due to high blood pressure over time)")
max_heart_rate = st.slider('Max Heart Rate' , 60, 220, 120, help="The highest heart rate achieved during physical exertion or a stress test, measured in beats per minute. A commonly used rough estimate for maximum heart rate is 220 minus your age. A lower-than-expected max heart rate can sometimes indicate heart problems")
exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'], help="Whether chest pain (angina) occurs specifically during physical exercise or exertion. Y = Yes, exercise triggers chest pain (a warning sign of reduced blood flow to the heart), N = No, no chest pain during exercise")
oldpeak = st.slider('Oldpeak (ST depression)', 0.0, 10.0, 1.0, help="The amount of ST segment depression on an ECG during exercise compared to rest, measured in millimeters. This reflects how much the heart's electrical activity changes under stress. A higher value generally indicates a greater likelihood of reduced blood flow (ischemia) to the heart")
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'], help="The slope (shape) of the ST segment during peak exercise on an ECG, which helps assess heart function under stress. Up = upsloping, usually considered a healthier pattern, Flat = flat slope, associated with higher risk, Down = downsloping, associated with the highest risk of heart disease")



if st.button('Predict'):
    # The generated column name must exactly match the column name used during model training.
    # Example: if sex = "M", this creates "Sex_M"; if sex = "F", it creates "Sex_F".
    # These generated names must match the model's training columns exactly.
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_heart_rate,
        'Oldpeak': oldpeak,
        'Sex_M': 1 if sex == 'Male' else 0,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }


    # Create a DataFrame with the input values
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # This helps to ensure that the input DataFrame has all the expected columns,
    # even if some of them are not present in the user input.
    # This is important because the model was trained with a specific set of features,
    # and it expects the same features during prediction.

    # Reorder the columns to match the expected order
    input_df = input_df[expected_columns]


    scaled_input = scaler.transform(input_df)


    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️ The model predicts that the patient has heart disease. Please consult a healthcare professional for further evaluation.")
    else:
        st.success("✅ The model predicts that the patient does not have heart disease. However, this is not a definitive diagnosis. Please consult a healthcare professional for further evaluation.")