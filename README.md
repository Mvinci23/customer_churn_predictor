# Customer Churn Prediction

## Business Problem
Customer churn is a critical challenge for telecom companies. Retaining existing customers is significantly more cost-effective than acquiring new ones. Being able to predict which customers are likely to leave allows businesses to proactively take actions such as targeted offers, improved support, or loyalty programs.

This project develops a **machine learning model to predict customer churn** using customer demographics, service subscriptions, and billing information.

The objective is to help telecom companies **identify high-risk customers and reduce churn using data-driven insights.**

---

# Dataset

The dataset contains telecom customer information including:

- Customer demographics
- Services subscribed
- Account details
- Billing information

### Dataset Characteristics

| Feature Type | Examples |
|--------------|----------|
| Categorical | Contract type, Internet service, Payment method |
| Numerical | Tenure, Monthly charges, Total charges |
| Target Variable | Churn (Yes / No) |

### Dataset Size

- **7043 customers**
- **21 features**
- Binary classification problem

---

# Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Prediction

---

# Exploratory Data Analysis

## Churn Distribution

![Churn Distribution](reports/figures/Chrun%20Distributions.png)

---

## Churn vs Paperless Billing

![Paperless Billing](reports/figures/Chrun%20distribution%20w.r.t.%20Paperless%20Billing.png)

---

## Churn vs Partner Status

![Partner](reports/figures/Chrun%20distribution%20w.r.t.%20Partners.png)

---

## Churn vs Phone Service

![Phone Service](reports/figures/Chrun%20distribution%20w.r.t.%20Phone%20Service.png)

---

## Churn vs Senior Citizen

![Senior Citizen](reports/figures/Chrun%20distribution%20w.r.t.%20Senior%20Citizen.png)

---

## Churn vs Tech Support

![Tech Support](reports/figures/Chrun%20distribution%20w.r.t.%20TechSupport.png)

---

## Churn vs Internet Service and Gender

![Internet Service](reports/figures/Chrun%20Distribution%20w.r.t.%20Internet%20Service%20and%20Gender.png)

---

## Churn vs Online Security

![Online Security](reports/figures/Churn%20w.r.t%20Online%20Security.png)

---

## Contract Distribution

![Contract](reports/figures/Customer%20contract%20distribution.png)

---

## Payment Method vs Churn

![Payment Method](reports/figures/Customer%20Payment%20Method%20distribution%20w.r.t.%20Churn.png)

---

## Dependents Distribution

![Dependents](reports/figures/Dependents%20distribution.png)

---

## Payment Method Distribution

![Payment Distribution](reports/figures/Payment%20Method%20Distribution.png)

---

## Tenure vs Churn

![Tenure](reports/figures/Tenure%20vs%20Churn.png)

---

# Machine Learning Models Used

Several classification models were trained and compared:

- Logistic Regression
- Random Forest
- Gradient Boosting
- Support Vector Machine
- Voting Classifier

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# Model Performance

Best model performance:

| Metric | Score |
|------|------|
| Accuracy | ~80% |
| ROC-AUC | ~0.84 |
| Precision | Balanced |
| Recall | Balanced |

The model demonstrates good ability to distinguish between customers likely to churn and those likely to stay.

---

# Key Insights

Important findings from the analysis:

- Customers with **month-to-month contracts churn the most**
- **Low tenure customers are more likely to churn**
- Customers without **tech support or online security services show higher churn**
- **Electronic check payments are associated with higher churn**
- Customers with **higher monthly charges have increased churn risk**

These insights can help telecom companies implement **targeted retention strategies.**

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

# Project Structure
customer_churn_predictor
│
├── reports
│ └── figures
│
├── Customer_churn_predictor_EDA.ipynb
├── churn.csv
├── final_churn_model.pkl
└── requirements.txt


---

# Future Improvements

Potential improvements include:

- Hyperparameter tuning
- Feature importance analysis
- Model explainability
- Real-time deployment
- Model monitoring

---

# Author

**Mondip Mech**

Machine Learning & Data Science Enthusiast
