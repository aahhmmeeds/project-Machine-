# 🏦 Customer Churn Prediction Model

## 📋 Project Overview
This project analyzes customer churn patterns using machine learning algorithms to predict which customers are likely to leave the bank. The model helps banks identify at-risk customers and take proactive measures to retain them.

## 🎯 Objective
- Predict customer churn using various machine learning algorithms
- Compare model performance across different algorithms
- Provide insights into factors that influence customer churn

## 📊 Dataset
The dataset contains customer information including:
- **CreditScore**: Customer's credit score
- **Geography**: Customer's location (France, Spain, Germany)
- **Gender**: Customer's gender
- **Age**: Customer's age
- **Tenure**: Number of years with the bank
- **Balance**: Account balance
- **NumOfProducts**: Number of products used
- **HasCrCard**: Whether customer has credit card
- **IsActiveMember**: Whether customer is active
- **EstimatedSalary**: Customer's estimated salary
- **Exited**: Target variable (1 = churned, 0 = retained)

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Scikit-learn** - Machine learning algorithms
- **XGBoost & LightGBM** - Gradient boosting
- **SMOTE** - Handling imbalanced data

## 🤖 Models Implemented
1. **Logistic Regression**
2. **Support Vector Machine (SVM)**
3. **K-Nearest Neighbors (KNN)**
4. **Decision Tree**
5. **Random Forest**
6. **XGBoost**
7. **LightGBM**
8. **AdaBoost**

## 📈 Model Evaluation Metrics
- **Accuracy**: Overall prediction accuracy
- **Precision**: True positive rate
- **Recall**: Sensitivity
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under ROC curve

## 🚀 How to Run
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place the `Churn_Modelling.csv` dataset in the project directory
3. Run the main script:
   ```bash
   python project1.py
   ```

## 📊 Key Findings
- Age and geography are significant factors in customer churn
- Customers with higher balances tend to have different churn patterns
- Model comparison shows Random Forest and XGBoost perform best

## 📁 Project Structure
```
Churn_Modelling/
├── project1.py          # Main analysis script
├── Churn_Modelling.csv  # Dataset (add your dataset here)
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

## 🔮 Future Improvements
- Feature engineering for better predictions
- Hyperparameter tuning
- Deep learning models
- Real-time prediction API

## 👨‍💻 Author
Machine Learning Project

---
⭐ If you find this project helpful, please give it a star!
