from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os

# Charger le dataset
data = pd.read_csv('/mnt/data/Customer_churn.csv')

# Prétraitement des données
# Supprimer les colonnes inutiles
data = data.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

# Encoder les variables catégorielles
label_encoders = {}
for column in ['Geography', 'Gender']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Diviser les données en features et target
X = data.drop(columns=['Exited'])
y = data['Exited']

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le dossier 'out' s'il n'existe pas
output_dir = "/mnt/data/out"
os.makedirs(output_dir, exist_ok=True)

# Ouverture du fichier score.txt en mode écriture
score_path = os.path.join(output_dir, "score.txt")
with open(score_path, "w") as f:

    # Étape 1 : Baseline sans ajustements
    baseline_model = RandomForestClassifier(random_state=42)
    baseline_model.fit(X_train, y_train)
    y_pred_baseline = baseline_model.predict(X_test)
    f1_baseline = f1_score(y_test, y_pred_baseline)
    accuracy_baseline = accuracy_score(y_test, y_pred_baseline)
    f.write("### Baseline Model (Sans ajustements) ###\n")
    f.write(f"F1-score: {f1_baseline:.2f}\n")
    f.write(f"Accuracy: {accuracy_baseline:.2f}\n\n")

    # Étape 2 : Modèle avec class_weight='balanced'
    balanced_model = RandomForestClassifier(class_weight='balanced', random_state=42)
    balanced_model.fit(X_train, y_train)
    y_pred_balanced = balanced_model.predict(X_test)
    f1_balanced = f1_score(y_test, y_pred_balanced)
    accuracy_balanced = accuracy_score(y_test, y_pred_balanced)
    f.write("### Modèle avec class_weight='balanced' ###\n")
    f.write(f"F1-score: {f1_balanced:.2f}\n")
    f.write(f"Accuracy: {accuracy_balanced:.2f}\n\n")

    # Étape 3 : Ajustement du seuil de décision (exemple avec un seuil de 0.3)
    y_proba = balanced_model.predict_proba(X_test)[:, 1]
    y_pred_threshold = (y_proba >= 0.3).astype(int)
    f1_threshold = f1_score(y_test, y_pred_threshold)
    accuracy_threshold = accuracy_score(y_test, y_pred_threshold)
    f.write("### Modèle avec ajustement du seuil (threshold=0.3) ###\n")
    f.write(f"F1-score: {f1_threshold:.2f}\n")
    f.write(f"Accuracy: {accuracy_threshold:.2f}\n\n")

# Retourner le chemin du fichier score.txt
score_path
