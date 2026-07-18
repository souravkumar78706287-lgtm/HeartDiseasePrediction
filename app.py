import pickle
import pandas as pd
import streamlit as st

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ HEART DISEASE PREDICTOR")
st.write("Predict Heart Disease using Multiple Machine Learning Models")

# -------------------- MODEL DETAILS --------------------

algonames = [
    "Decision Tree",
    "Random Forest",
    "Logistic Regression",
    "SVM"
]

modelnames = [
    "decisiontree.pkl",
    "randomforest.pkl",
    "logisticr.pkl",
    "svm.pkl"
]

# -------------------- LOAD MODELS ONLY ONCE --------------------

@st.cache_resource
def load_models():
    models = []
    for modelname in modelnames:
        with open(modelname, "rb") as file:
            models.append(pickle.load(file))
    return models

models = load_models()

# -------------------- PREDICTION FUNCTION --------------------

def predict_heart_disease(input_df):
    predictions = []
    for model in models:
        prediction = model.predict(input_df)
        predictions.append(prediction)
    return predictions

# -------------------- DOWNLOAD FUNCTION --------------------

def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

# -------------------- TABS --------------------

tab1, tab2, tab3 = st.tabs(
    [
        "🔍 Single Prediction",
        "📂 Bulk Prediction",
        "📊 Model Information"
    ]
)

# ==========================================
# TAB 1 : SINGLE PREDICTION
# ==========================================
with tab1:
    st.header("👤 Patient Details")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (Years)", 0, 150, 45)
        sex = st.selectbox("Sex", ["male", "female"])
        chest_pain = st.selectbox(
            "Chest Pain Type",
            [
                "typical angina",
                "atypical angina",
                "non-anginal pain",
                "asymptomatic"
            ]
        )
        resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 0, 250, 120)
        cholesterol = st.number_input("Cholesterol (mg/dl)", 0, 700, 200)

    with col2:
        max_hr = st.number_input("Maximum Heart Rate", 0, 250, 150)
        fasting_bs = st.selectbox("Fasting Blood Sugar >120 mg/dl", ["yes", "no"])
        resting_ecg = st.selectbox(
            "Resting ECG",
            [
                "normal",
                "st-t wave abnormality",
                "left ventricular hypertrophy"
            ]
        )
        exercise_angina = st.selectbox("Exercise Induced Angina", ["yes", "no"])
        oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
        st_slope = st.selectbox(
            "ST Slope",
            [
                "upsloping",
                "flat",
                "downsloping"
            ]
        )

    # Encoding Maps
    sex_encoded = 0 if sex == "male" else 1
    chest_pain_encoded = ["atypical angina", "non-anginal pain", "asymptomatic", "typical angina"].index(chest_pain)
    fasting_bs_encoded = 1 if fasting_bs == "yes" else 0
    resting_ecg_encoded = ["normal", "st-t wave abnormality", "left ventricular hypertrophy"].index(resting_ecg)
    exercise_angina_encoded = 1 if exercise_angina == "yes" else 0
    st_slope_encoded = ["upsloping", "flat", "downsloping"].index(st_slope)

    # Create Input DataFrame matching feature names exactly
    input_data = pd.DataFrame({
        "Age": [age],
        "RestingBP": [resting_bp],
        "Cholesterol": [cholesterol],
        "FastingBS": [fasting_bs_encoded],
        "MaxHR": [max_hr],
        "Oldpeak": [oldpeak],

        "Sex_0": [1 if sex_encoded == 0 else 0],
        "Sex_1": [1 if sex_encoded == 1 else 0],

        "ChestPainType_0": [1 if chest_pain_encoded == 0 else 0],
        "ChestPainType_1": [1 if chest_pain_encoded == 1 else 0],
        "ChestPainType_2": [1 if chest_pain_encoded == 2 else 0],
        "ChestPainType_3": [1 if chest_pain_encoded == 3 else 0],

        "RestingECG_0": [1 if resting_ecg_encoded == 0 else 0],
        "RestingECG_1": [1 if resting_ecg_encoded == 1 else 0],
        "RestingECG_2": [1 if resting_ecg_encoded == 2 else 0],

        "ExerciseAngina_0": [1 if exercise_angina_encoded == 0 else 0],
        "ExerciseAngina_1": [1 if exercise_angina_encoded == 1 else 0],

        "ST_Slope_0": [1 if st_slope_encoded == 0 else 0],
        "ST_Slope_1": [1 if st_slope_encoded == 1 else 0],
        "ST_Slope_2": [1 if st_slope_encoded == 2 else 0]
    })

    st.divider()

    if st.button("🔍 Predict Heart Disease", type="primary"):
        predictions = predict_heart_disease(input_data)
        st.subheader("Prediction Results")

        result_df = pd.DataFrame({
            "Model": algonames,
            "Prediction": [
                int(predictions[0][0]),
                int(predictions[1][0]),
                int(predictions[2][0]),
                int(predictions[3][0])
            ]
        })

        st.dataframe(result_df, use_container_width=True)
        st.divider()

        for i in range(len(predictions)):
            if predictions[i][0] == 1:
                st.error(f"🚨 {algonames[i]} predicts that the patient HAS Heart Disease.")
            else:
                st.success(f"✅ {algonames[i]} predicts that the patient DOES NOT have Heart Disease.")

# ==========================================
# TAB 2 : BULK PREDICTION
# ==========================================
with tab2:
    st.header("📂 Bulk Heart Disease Prediction")
    st.info("""
    Upload a CSV file containing these 11 essential columns:
    `Age`, `Sex`, `ChestPainType`, `RestingBP`, `Cholesterol`, `FastingBS`, `RestingECG`, `MaxHR`, `ExerciseAngina`, `Oldpeak`, `ST_Slope`
    """)

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        expected_columns = [
            'Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
            'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'
        ]

        if all(col in df.columns for col in expected_columns):
            model_df = pd.DataFrame()
            
            # Map structural components
            model_df["Age"] = df["Age"]
            model_df["RestingBP"] = df["RestingBP"]
            model_df["Cholesterol"] = df["Cholesterol"]
            model_df["FastingBS"] = df["FastingBS"]
            model_df["MaxHR"] = df["MaxHR"]
            model_df["Oldpeak"] = df["Oldpeak"]

            # Sex Category Encodings
            model_df["Sex_0"] = (df["Sex"] == 0).astype(int)
            model_df["Sex_1"] = (df["Sex"] == 1).astype(int)

            # Chest Pain Encodings
            for i in range(4):
                model_df[f"ChestPainType_{i}"] = (df["ChestPainType"] == i).astype(int)

            # ECG Encodings
            for i in range(3):
                model_df[f"RestingECG_{i}"] = (df["RestingECG"] == i).astype(int)

            # Angina Encodings
            model_df["ExerciseAngina_0"] = (df["ExerciseAngina"] == 0).astype(int)
            model_df["ExerciseAngina_1"] = (df["ExerciseAngina"] == 1).astype(int)

            # ST Segment Slope Encodings
            for i in range(3):
                model_df[f"ST_Slope_{i}"] = (df["ST_Slope"] == i).astype(int)

            # Run Matrix Evaluation
            predictions = predict_heart_disease(model_df)
            result = df.copy()

            result["Decision Tree"] = predictions[0]
            result["Random Forest"] = predictions[1]
            result["Logistic Regression"] = predictions[2]
            result["SVM"] = predictions[3]

            st.success("🎉 Prediction Matrix Generation Completed!")
            st.dataframe(result, use_container_width=True)

            csv = convert_df(result)
            st.download_button(
                label="📥 Download Compiled Batch Predictions",
                data=csv,
                file_name="heart_disease_bulk_predictions.csv",
                mime="text/csv",
                type="primary"
            )
        else:
            st.error("❌ The uploaded CSV schema does not contain the required header arrays.")
    else:
        st.info("💡 Please upload a clean CSV file format to start process evaluation arrays.")

# ==========================================
# TAB 3 : MODEL INFORMATION
# ==========================================
with tab3:
    st.header("📊 Model Performance Details")

    accuracy = pd.DataFrame({
        "Model": ["Decision Tree", "Random Forest", "Logistic Regression", "SVM"],
        "Accuracy (%)": [88.98, 90.16, 86.88, 87.70]
    })

    col_metrics, col_chart = st.columns([1, 2])
    
    with col_metrics:
        st.subheader("Accuracy Matrix Table")
        st.dataframe(accuracy, use_container_width=True, hide_index=True)

    with col_chart:
        st.subheader("Performance Spread Chart")
        st.bar_chart(accuracy.set_index("Model"))

    st.markdown("---")
    st.markdown("""
    ### Dataset Profile
    Evaluations compiled against reference UCI / Heart Disease Prediction Datasets.

    ### Metric Arrays Extracted
    *   **Vitals Tracking:** Resting Blood Pressure (`RestingBP`), Serum Cholesterol (`Cholesterol`), Maximum Heart Rate (`MaxHR`), Fasting Blood Sugar Baseline (`FastingBS`).
    *   **Electrocardiogram Features:** ST Depression (`Oldpeak`), Peak Exercise ST Segment Slope (`ST_Slope`), Resting ECG Vitals Matrix (`RestingECG`).
    *   **Physical Markers:** Chest Pain Typology Classifications (`ChestPainType`), Angina Symptom Inductions (`ExerciseAngina`).
    """)