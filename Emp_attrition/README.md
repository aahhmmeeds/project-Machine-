# 👥 HR Employee Attrition Prediction App

## 📋 Project Overview
An interactive Streamlit web application that predicts employee attrition using machine learning. This tool helps HR departments identify employees at risk of leaving and take proactive retention measures.

## 🎯 Objective
- Predict employee attrition probability using Random Forest algorithm
- Provide interactive web interface for HR professionals
- Visualize model performance and prediction results
- Enable real-time predictions for new employee data

## 📊 Dataset Features
- **Employee demographics and job information**
- **Performance metrics**
- **Work environment factors**
- **Compensation details**
- **Target**: Attrition (Stayed/Left)

## 🛠️ Technologies Used
- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning
- **SMOTE** - Handling imbalanced data
- **Plotly** - Interactive visualizations
- **Matplotlib & Seaborn** - Data visualization

## 🤖 Model Details
- **Algorithm**: Random Forest Classifier
- **Data Balancing**: SMOTE (Synthetic Minority Oversampling Technique)
- **Preprocessing**: Label encoding for categorical variables
- **Evaluation**: Accuracy, Precision, Recall, F1-Score

## 🚀 How to Run
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure `Emp_attrition_csv.csv` is in the project directory
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser to `http://localhost:8501`

## 📱 App Features
- **Dataset Preview**: View the first few rows of the dataset
- **Model Performance**: Real-time accuracy metrics
- **Confusion Matrix**: Interactive visualization
- **Employee Prediction**: Input employee details for prediction
- **Probability Visualization**: Pie chart showing prediction confidence

## 📊 Model Performance
The app displays both training and testing metrics:
- Accuracy scores
- Precision rates
- Recall rates
- F1-scores

## 📁 Project Structure
```
Emp_attrition/
├── app.py                    # Main Streamlit application
├── Emp_attrition_csv.csv     # Employee dataset
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

## 🔮 Future Enhancements
- Model comparison dashboard
- Feature importance analysis
- Historical trend analysis
- Export prediction reports
- Integration with HR systems

## 👨‍💻 Author
Machine Learning Project

---
⭐ If you find this project helpful, please give it a star!
