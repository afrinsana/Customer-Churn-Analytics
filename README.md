# Customer Churn Analytics

A data-driven end-to-end solution to identify customers who are likely to churn — and uncover the key drivers behind their behavior. This project combines exploratory data analysis, feature engineering, model building, and actionable insights to empower data-backed business decisions.

---

## Problem Statement

Customer retention is crucial for long-term profitability. Losing customers leads to loss of revenue and increased acquisition costs. This project aims to build a predictive model to:

- Identify customers at risk of churning.
- Understand factors that contribute to churn.
- Help the business take proactive steps to reduce churn.

---

## Project Pipeline

*1. Data Collection & Cleaning*
- Imported real-world telecom churn dataset.
- Handled missing values, inconsistent formatting, and irrelevant features.

*2. Exploratory Data Analysis (EDA)*
- Uncovered patterns, outliers, and correlations using pandas, seaborn, and matplotlib.
- Identified key trends in customer behavior by segment (e.g., contract type, tenure, support calls).

*3. Feature Engineering*
- Encoded categorical features.
- Created new features like tenure groups, service count, and avg monthly spend.

*4. Model Building*
- Applied multiple classification algorithms:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Evaluated using accuracy, precision, recall, F1-score, and ROC-AUC.

*5. Model Selection*
- Chose the best-performing model based on business relevance and metrics.

*6. Interpretation & Insights*
- Visualized feature importance.
- Created actionable insights to reduce churn, such as:
  - Offering loyalty benefits to high-risk tenure groups.
  - Improving support for tech-savvy customers using multiple services.

---

## Tools & Technologies

- *Languages*: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- *IDE*: Jupyter Notebook
- *Version Control*: Git & GitHub
- *Model Evaluation*: Confusion Matrix, ROC-AUC, Precision-Recall Curve

---

## Project Highlights

- Achieved *~85% accuracy* using XGBoost Classifier.
- Built a reusable pipeline for preprocessing and model deployment.
- Visual dashboard for key churn indicators (upcoming: Streamlit version).

---

## Folder Structure
Customer_Churn_Analytics/
│
├── app.py                        # Script for model and dashboard (future-ready)
├── Customer_Churn_Model_Training.ipynb  # Jupyter notebook with full pipeline
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview
└── .gitignore                    # Ignored files
---

## Future Enhancements

- Integrate *Streamlit* to deploy an interactive dashboard.
- Use *AWS/Azure* for hosting and scalability.
- Automate retraining pipeline with CI/CD workflows.

---

## Author

*Afrin Sana*  
Data Science & Machine Learning Enthusiast  
[LinkedIn](https://www.linkedin.com/in/afrinsana/) | [GitHub](https://github.com/afrinsana)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
