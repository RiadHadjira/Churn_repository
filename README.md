# 				Prédiction Churn Secteur Bancaire
## 	Description du Projet

Le projet **Prédiction Churn Secteur Bancaire** vise à anticiper les risques d’abandon des clients en utilisant un modèle de machine learning. Grâce à un modèle RandomForest optimisé, cette application permet aux institutions financières de cibler les clients susceptibles de quitter la banque. En analysant le comportement des clients, l'application aide à adapter les stratégies de rétention de manière proactive, améliorant ainsi la fidélisation client.

L’application a été développée en Python avec Flask pour le backend API et Streamlit pour l’interface utilisateur, rendant l’outil intuitif et interactif pour une utilisation en temps réel.

## 	Business Use Case (BUC)
Le churn représente une perte importante pour les institutions bancaires, et la capacité à prédire les clients à risque de départ peut fortement contribuer à optimiser les stratégies de rétention. Ce projet vise donc à fournir un modèle prédictif pour identifier les clients à risque, permettant de cibler les efforts de rétention de manière plus efficace.

## 	Dataset
Le dataset utilisé, Customer_churn.csv, contient des informations sur 10 000 clients et inclut les caractéristiques suivantes :

- **RowNumber** : Numéro de ligne dans le dataset.
- **CustomerId** : Identifiant unique du client.
- **Surname** : Nom de famille du client.
- **CreditScore** : Score de crédit du client.
- **Geography** : Pays de résidence (France, Espagne, etc.).
- **Gender** : Sexe du client (Male ou Female).
- **Age** : Âge du client.
- **Tenure** : Durée de la relation avec la banque (en années).
- **Balance** : Solde actuel du client.
- **NumOfProducts** : Nombre de produits bancaires souscrits par le client.
- **HasCrCard** : Indicateur de possession d'une carte de crédit (1 = Oui, 0 = Non).
- **IsActiveMember** : Indicateur de l'activité du client (1 = Actif, 0 = Inactif).
- **EstimatedSalary** : Salaire estimé du client.
- **Exited** : Variable cible indiquant si le client a quitté la banque (1 = Oui, 0 = Non).
Ces données permettent d’analyser les comportements clients et de prédire les départs potentiels.

## 	Baseline
Pour la version de base du modèle :

- **Caractéristiques utilisées** : Toutes les caractéristiques disponibles sauf CustomerId, Surname, et RowNumber.
- **Pré-traitement** : Encodage des variables catégorielles (Geography, Gender), normalisation des valeurs numériques, gestion des valeurs manquantes.
- **Modèle initial** : Un modèle RandomForest sans ajustements particuliers a été utilisé pour obtenir une première version.
- **Métrique obtenue** : F1-score de 57% sur l'ensemble de test.

## 	Première itération
Des améliorations ont été apportées pour optimiser le modèle :

- **Modifications** : Ajustement du seuil de décision, utilisation de class_weight='balanced', et application de SMOTE pour équilibrer les classes.
- **Pourquoi ces changements** : Le dataset présentait un déséquilibre de classes, rendant difficile la prédiction du churn avec précision. L'ajustement du seuil et l'utilisation de SMOTE ont permis d'améliorer la détection des clients à risque.
- **Impact sur les métriques** : Après optimisation, le F1-score a atteint 61%, ce qui représente une amélioration de 4% par rapport à la baseline.

## 	Fonctionnalités de l'Application
- **Prédiction du Churn** : Entrez le numéro d’un client et obtenez instantanément une prédiction sur son risque de churn (churner ou non) avec une probabilité associée.
- **Analyse et Exploration des Données** : Interface dédiée pour explorer les données clients et comprendre les tendances de churn.
- **Optimisation de la Rétention** : Aide les banques à identifier les clients à risque pour adapter leurs stratégies de fidélisation.

## 	Installation et Pré-requis

- **Cloner le dépôt** :

git clone https://github.com/RiadHadjira/Churn_repository

- **Installer les dépendances** : Installez les bibliothèques requises avec :

pip install -r requirements.txt

- **Lancer l’API Flask** : Depuis le dossier principal, lancez le serveur Flask :
python app.py

- **Lancer l'interface Streamlit** : Dans un nouveau terminal, exécutez la commande suivante pour démarrer l'interface utilisateur :
streamlit run streamlit_app.py

## 	Utilisation

- **Démarrer l’Application** : Après avoir lancé Flask et Streamlit, accédez à l’interface via le lien fourni par Streamlit (généralement http://localhost:8501).
- **Explorer les Données** : Accédez à l’onglet d'exploration des données pour visualiser les caractéristiques des clients et les tendances de churn.
- **Prédire le Churn** : Dans l’onglet de prédiction, entrez le numéro d’un client pour obtenir la probabilité de churn associée et savoir s’il est à risque ou non.

## 	Structure du Code

- **app.py** : Contient le code de l’API Flask pour gérer les requêtes de prédiction.
- **streamlit_app.py** : Fichier Streamlit pour l’interface utilisateur, comprenant les onglets pour l’exploration des données et la prédiction du churn.
- **random_forest_model.pkl** : Fichier sauvegardé du modèle RandomForest entraîné.
- **Customer_churn.csv** : Dataset contenant les informations client.
**Projet_ML.ipynb** : Notebook pour l’analyse exploratoire des données (EDA) et la création du modèle de base.
**requirements.txt** : Fichier listant les dépendances du projet.

## 	Script autonome
Un script script.py est inclus pour une utilisation simplifiée :

- **Chargement des données** : Charge automatiquement le dataset Customer_churn.csv.
- **Entraînement du modèle** : Entraîne un modèle RandomForest avec les caractéristiques définies.
- **Calcul des métriques** : Calcule et sauvegarde les métriques de performance (F1-score) dans out/score.txt.
## 	Technologies Utilisées
**Python** : Langage principal pour le développement de l’application.
**Flask** : Framework léger pour construire l’API backend.
**Streamlit** : Bibliothèque pour créer l’interface utilisateur interactive.
**Scikit-Learn** : Utilisé pour le modèle RandomForest et le prétraitement des données.
**Pandas & NumPy** : Pour la manipulation et l’analyse des données.
**SMOTE (imbalanced-learn)** : Pour équilibrer les classes en ajustant la distribution des données.

## 	Auteurs

Développé par Elias Pianko Hadjira Riad.  
