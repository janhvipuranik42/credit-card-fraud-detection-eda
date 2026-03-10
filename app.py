import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Credit Card Fraud Detection - EDA Dashboard")

# Load dataset
df = pd.read_csv("creditcard.csv")

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Dataset shape
st.subheader("Dataset Shape")
st.write(df.shape)

# Fraud vs Normal count
st.subheader("Fraud vs Normal Transactions")

fig1, ax1 = plt.subplots()
sns.countplot(x='Class', data=df, ax=ax1)
st.pyplot(fig1)

# Transaction Amount Distribution
st.subheader("Transaction Amount Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(df['Amount'], bins=50, ax=ax2)
st.pyplot(fig2)

# Fraud vs Normal Amount
st.subheader("Fraud vs Normal Transaction Amount")

fig3, ax3 = plt.subplots()
sns.boxplot(x='Class', y='Amount', data=df, ax=ax3)
st.pyplot(fig3)

# Correlation Heatmap
st.subheader("Correlation Heatmap")

fig4, ax4 = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), cmap='coolwarm', ax=ax4)
st.pyplot(fig4)

# Conclusion
st.subheader("Conclusion")

st.write("""
Fraudulent transactions are extremely rare compared to normal transactions.
EDA helps identify patterns in transaction behavior which can be useful
for building fraud detection machine learning models.
""")