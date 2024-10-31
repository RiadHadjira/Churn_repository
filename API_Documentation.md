
# Documentation de l'API Flask - Prédiction Churn Secteur Bancaire

Cette API Flask permet de faire des prédictions de churn pour des clients bancaires à partir d'un modèle de machine learning. 

## Endpoints de l'API

### 1. `GET /predict`

#### Description
Cet endpoint accepte les caractéristiques d'un client et retourne la probabilité que ce client quitte la banque (churn).

#### URL
`/predict`

#### Méthode
`GET`

#### Paramètres attendus
Les paramètres sont passés en tant que query parameters dans l'URL. Voici les caractéristiques requises :
- `CreditScore` (int) : Score de crédit du client.
- `Geography` (string) : Pays de résidence du client (ex : 'France', 'Spain').
- `Gender` (string) : Sexe du client ('Male' ou 'Female').
- `Age` (int) : Âge du client.
- `Tenure` (int) : Durée de la relation avec la banque (en années).
- `Balance` (float) : Solde actuel du client.
- `NumOfProducts` (int) : Nombre de produits bancaires souscrits.
- `HasCrCard` (int) : Possession d'une carte de crédit (1 = Oui, 0 = Non).
- `IsActiveMember` (int) : Statut d'activité du client (1 = Actif, 0 = Inactif).
- `EstimatedSalary` (float) : Salaire estimé du client.

#### Exemple de requête
```bash
curl -X GET "http://localhost:5000/predict?CreditScore=600&Geography=France&Gender=Male&Age=40&Tenure=5&Balance=100000&NumOfProducts=2&HasCrCard=1&IsActiveMember=1&EstimatedSalary=50000"
```

#### Réponse
La réponse est au format JSON et contient :
- `churn` : La classe prédite pour le client (1 = churn, 0 = non-churn).
- `probability` : La probabilité associée à la prédiction.

#### Exemple de réponse
```json
{
  "churn": 1,
  "probability": 0.75
}
```

## Utilisation

1. Assurez-vous que l'API Flask est lancée (exécutez `python app.py`).
2. Envoyez une requête `GET` à l'endpoint `/predict` en passant les caractéristiques du client en tant que query parameters.

## Remarques

- Les valeurs des paramètres doivent être fournies dans le bon type (par exemple, `Balance` et `EstimatedSalary` en `float`, `Age` en `int`).
- Le modèle de prédiction est entraîné pour des données spécifiques, et les résultats peuvent varier en fonction de l'optimisation et des mises à jour du modèle.

---

Cette documentation est conçue pour faciliter l'interaction avec l'API et donner aux développeurs les informations nécessaires pour intégrer le service de prédiction de churn.
