import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="HR Attrition Predictor", layout="wide", page_icon="📊")
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 HR Attrition Prediction App")
st.markdown("Use employee details to predict the likelihood of attrition using a Random Forest model.")

@st.cache_data
def load_data():
    df = pd.read_csv("Emp_attrition_csv.csv")
    df.drop(['Employee ID'], axis=1, inplace=True, errors='ignore')
    df['Attrition'] = df['Attrition'].map({'Stayed': 0, 'Left': 1})
    df['Distance from Home'].fillna(df['Distance from Home'].mean(), inplace=True)
    df['Company Tenure (In Months)'].fillna(df['Company Tenure (In Months)'].mean(), inplace=True)
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders

df, label_encoders = load_data()

st.markdown("---")
st.subheader("📁 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

X = df.drop('Attrition', axis=1)
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, y_train = SMOTE(random_state=42).fit_resample(X_train, y_train)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

st.markdown("---")
st.subheader("📈 Model Evaluation")

col1, col2 = st.columns(2)
with col1:
    st.metric("Train Accuracy", f"{accuracy_score(y_train, y_pred_train)*100:.2f}%")
    st.metric("Train Precision", f"{precision_score(y_train, y_pred_train)*100:.2f}%")
    st.metric("Train Recall", f"{recall_score(y_train, y_pred_train)*100:.2f}%")
    st.metric("Train F1", f"{f1_score(y_train, y_pred_train)*100:.2f}%")
with col2:
    st.metric("Test Accuracy", f"{accuracy_score(y_test, y_pred_test)*100:.2f}%")
    st.metric("Test Precision", f"{precision_score(y_test, y_pred_test)*100:.2f}%")
    st.metric("Test Recall", f"{recall_score(y_test, y_pred_test)*100:.2f}%")
    st.metric("Test F1", f"{f1_score(y_test, y_pred_test)*100:.2f}%")

st.markdown("---")
st.subheader("🔍 Confusion Matrix")
cm = confusion_matrix(y_test, y_pred_test)
fig = px.imshow(cm, text_auto=True, x=["Stayed", "Left"], y=["Stayed", "Left"],
                labels=dict(x="Predicted", y="Actual", color="Count"),
                color_continuous_scale='Blues', title="Confusion Matrix")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🔮 Predict Attrition for a New Employee")

user_input = {}
for col in X.columns:
    if col in label_encoders:
        options = label_encoders[col].classes_.tolist()
        user_val = st.selectbox(f"{col}", options)
        user_input[col] = label_encoders[col].transform([user_val])[0]
    else:
        user_input[col] = st.number_input(f"{col}", value=float(X[col].mean()))

if st.button("🔍 Predict Attrition"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    result = "🔴 Employee is likely to leave." if prediction == 1 else "🟢 Employee is likely to stay."
    st.success(result)

    proba = model.predict_proba(input_df)[0]
    fig = go.Figure(go.Pie(labels=["Stay", "Leave"], values=[proba[0], proba[1]],
                           marker=dict(colors=["green", "red"])))
    fig.update_traces(hole=0.4, hoverinfo="label+percent")
    fig.update_layout(title="Prediction Probability", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
