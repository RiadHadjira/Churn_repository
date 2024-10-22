from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load dataset
df_path = "Customer_churn.csv"
df = pd.read_csv(df_path)
df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
df = pd.get_dummies(df, columns=['Geography'], drop_first=True)
# Load models

with open("random_forest_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON request data
    data = request.get_json()

    # Check if customer_id is provided
    customer_id = data.get("CustomerId")
    if not customer_id:
        return jsonify({"error": "No customer_id provided"}), 400

    # Find customer data in the dataset
    customer_data = df[df["CustomerId"] == customer_id]
    # Label encoding pour Gender et Geography
    if customer_data.empty:
        return jsonify({"error": "Customer ID not found"}), 404
    # Extract features (excluding 'customer_id' and 'default')
    features = customer_data.drop(columns=['RowNumber', 'CustomerId', 'Surname','Exited']).values

    # Scale the features if necessary (e.g., use the scaler applied during training)
    # Here, assuming features are already scaled if models are trained on scaled data

    # Random Forest prediction
    rf_pred = rf_model.predict(features)
    rf_proba = rf_model.predict_proba(features)[:, 1]

    # Respond with predictions
    return jsonify({
        "CustomerId": customer_id,
        "rf_prediction": int(rf_pred[0]),
        "rf_probability": float(rf_proba[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
