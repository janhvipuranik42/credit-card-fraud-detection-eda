Credit Card Fraud Detection – Exploratory Data Analysis (EDA)
This project performs Exploratory Data Analysis (EDA) on a credit card transaction dataset to understand patterns between fraudulent and legitimate transactions. The analysis focuses on identifying trends, visualizing data distributions, and exploring correlations between features that may indicate fraudulent activity.

Dataset

The dataset used in this project is the Credit Card Fraud Detection.

Dataset link:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud⁠�

The dataset contains credit card transactions made by European cardholders in September 2013.
Dataset Features
Total transactions: 284,807
Number of features: 31
Highly imbalanced dataset
Target column: Class
0 → Normal transaction
1 → Fraudulent transaction

Technologies Used

Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook
Analysis Performed

The following analysis was performed in this project:
Dataset overview and structure analysis
Checking missing values
Fraud vs normal transaction distribution
Transaction amount distribution analysis
Fraud transaction amount analysis
Correlation heatmap visualization
Fraud percentage visualization

Key Insights

Fraudulent transactions represent a very small percentage of total transactions, making the dataset highly imbalanced.
Most transactions occur with small transaction amounts.
Data visualization helps reveal patterns and differences between fraudulent and legitimate transactions.

Project Structure

credit-card-fraud-detection-eda
│
├── credit_card_fraud_detection_eda.ipynb
└── README.md

Conclusion

This project demonstrates how Exploratory Data Analysis can help understand fraud patterns in financial transactions. The insights obtained from EDA can be useful for building machine learning models for fraud detection in financial systems.
