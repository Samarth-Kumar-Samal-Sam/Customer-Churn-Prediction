# =============================================================================
# Import required libraries
# =============================================================================
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from PIL import Image

# =============================================================================
# Load the trained pipeline once during app startup
# =============================================================================
MODEL_PATH = Path(__file__).with_name("Models") / "Logistic_Pipeline.pkl"

@st.cache_resource(show_spinner=False)
def load_pipeline(path: Path):
    if not path.exists():
        st.error(f"Model file not found at: {path.resolve()}")
        st.stop()
    with path.open("rb") as f:
        pipeline = joblib.load(f)
    return pipeline

lor = load_pipeline(MODEL_PATH)

# =============================================================================
# Define the feature schema used by the trained model
# =============================================================================
FEATURES = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
    "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
    "MonthlyCharges", "TotalCharges"
]

# =============================================================================
# Define helper mappings (for display logic if needed)
# =============================================================================
YES_NO = {"Yes": "Yes", "No": "No"}
YES_NO_INT = {"Yes": 1, "No": 0}

# =============================================================================
# Building the Streamlit Web Application UI
# =============================================================================
churn_image = Image.open("Assets/Churn_Image.png")
st.image(churn_image, use_container_width=True)

st.title("Customer Churn Predictor")

st.markdown(
    "Enter customer details in the form below and click **Predict** "
    "to see whether the customer is likely to churn."
)

with st.form("churn_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        senior = st.radio("Senior Citizen", list(YES_NO_INT.keys()), horizontal=True)
        partner = st.radio("Has Partner", list(YES_NO.keys()), horizontal=True)
        dependents = st.radio("Has Dependents", list(YES_NO.keys()), horizontal=True)
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
        phone_service = st.radio("Phone Service", list(YES_NO.keys()), horizontal=True)
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"], index=0)
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], index=0)

    with col2:
        online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"], index=0)
        online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"], index=0)
        device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"], index=0)
        tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"], index=0)
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"], index=0)
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"], index=0)
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], index=0)
        paperless_billing = st.radio("Paperless Billing", list(YES_NO.keys()), horizontal=True)
        payment_method = st.selectbox(
            "Payment Method",
            ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
            index=0,
        )
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, step=0.1, value=70.0)
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, step=0.1, value=2500.0)

    submitted = st.form_submit_button("🔮 Predict", type="primary")

# =============================================================================
# Prediction Logic
# =============================================================================
if submitted:
    senior = "Yes" if senior == 1 else "No"

    row = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
    })

    categorical_cols = row.select_dtypes(include=["object"]).columns.tolist()
    for col in categorical_cols:
        le = LabelEncoder()
        row[col] = le.fit_transform(row[col])

    row = row[FEATURES]

    try:
        proba = lor.predict_proba(row)[0][1]
        pred = "Churn" if proba >= 0.5 else "Not Churn"

        if pred == "Churn":
            st.markdown(f"<h4 style='color:green;'>✅ Prediction: {pred}</h4>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h4 style='color:red;'>⚠️ Prediction: {pred}</h4>", unsafe_allow_html=True)

        st.metric("Churn Probability", f"{proba:.1%}")

    except Exception as e:
        st.error("Prediction failed. Please check model compatibility.")
        st.exception(e)
