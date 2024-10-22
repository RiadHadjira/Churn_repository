import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df_path = "Customer_churn.csv"
df = pd.read_csv(df_path)

# Title
st.title("Loan Default Prediction and Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Data Visualization", "Make Predictions"])

# Data Visualization Section
if section == "Data Visualization":
    st.header("Data Visualization")

    # Visualize numeric variables
    st.subheader("Numeric Variable Distributions by Default")

    numeric_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
    for col in numeric_columns:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(data=df, x=col, hue='Exited', multiple='stack', bins=30, ax=ax)
        ax.set_title(f'Distribution of {col} by Default')
        st.pyplot(fig)

    # Visualize categorical variables
    st.subheader("Categorical Variable Distributions by Default")

    categorical_columns = ['Gender', 'Geography', 'HasCrCard', 'IsActiveMember']
    for col in categorical_columns:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.countplot(data=df, x=col, hue='Exited', ax=ax)
        ax.set_title(f'{col} Distribution by Default')
        st.pyplot(fig)

    # Correlation matrix for numeric columns
    st.subheader("Correlation Matrix")

    # Only select numeric columns
    numeric_df = df.select_dtypes(include=[np.number])

    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    # Encode categorical columns for correlation matrix
    st.subheader("Correlation Matrix with Encoded Categorical Variables")

    # Encoding the Gender column
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])

    # Use pd.get_dummies to encode Geography and other categorical columns
    df = pd.get_dummies(df, columns=['Geography'], drop_first=True)

    # Recalculate correlation matrix after encoding categorical variables
    encoded_numeric_df = df.select_dtypes(include=[np.number])

    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = encoded_numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Correlation Matrix (with Encoded Categorical Variables)')
    st.pyplot(fig)

# Prediction Section
elif section == "Make Predictions":
    st.header("Predict Loan Default for a Customer")

    # Dropdown to select customer ID
    customer_ids = df['CustomerId'].unique()
    selected_id = st.selectbox("Select Customer ID", customer_ids)

    # Button to trigger prediction
    if st.button("Predict"):
        # Call the Flask API
        selected_id = int(selected_id)
        try:
            response = requests.post("http://127.0.0.1:5000/predict", json={"CustomerId": selected_id})
            if response.status_code == 200:
                prediction = response.json()

                # Display the prediction
                st.subheader(f"Prediction for Customer ID: {selected_id}")
                st.write(f"Random Forest Prediction: {prediction['rf_prediction']}")
                st.write(f"Random Forest Probability: {prediction['rf_probability']:.2f}")
            else:
                st.error("Error in prediction: " + response.text)

        except Exception as e:
            st.error(f"Error connecting to the Flask app: {e}")
