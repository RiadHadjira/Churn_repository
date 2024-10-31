                                                                Prédiction Churn Secteur Bancaire

	  Description du Projet

Le projet Prédiction Churn Secteur Bancaire vise à anticiper les risques d’abandon des clients en utilisant un modèle de machine learning. 
Grâce à un modèle RandomForest optimisé, cette application permet aux institutions financières de cibler les clients susceptibles de quitter la banque. 
En analysant le comportement des clients, l'application aide à adapter les stratégies de rétention de manière proactive, améliorant ainsi la fidélisation client.

L’application a été développée en Python avec Flask pour le backend API et Streamlit pour l’interface utilisateur, rendant l’outil intuitif et interactif pour une utilisation en temps réel.

	  Fonctionnalités de l'Application

- Prédiction du Churn : Entrez le numéro d’un client et obtenez instantanément une prédiction sur son risque de churn (churner ou non) avec une probabilité associée.
- Analyse et Exploration des Données : Interface dédiée pour explorer les données clients et comprendre les tendances de churn.
- Optimisation de la Rétention : Aide les banques à identifier les clients à risque pour adapter leurs stratégies de fidélisation.

	  Installation et Pré-requis

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/RiadHadjira/Churn_repository
   ```

2. Installer les dépendances :
Installez les bibliothèques requises avec :
   ```bash
   pip install -r requirements.txt
   ```

3. *Lancer l’API Flask :
   Depuis le dossier principal, lancez le serveur Flask :
   ```bash
   python app.py
   ```

4. Lancer l'interface Streamlit :
   Dans un nouveau terminal, exécutez la commande suivante pour démarrer l'interface utilisateur :
   ```bash
   streamlit run interface.py
   ```

	    Utilisation

1. Démarrer l’Application : Après avoir lancé Flask et Streamlit, accédez à l’interface via le lien fourni par Streamlit (généralement `http://localhost:8501`).
2. Explorer les Données : Accédez à l’onglet d'exploration des données pour visualiser les caractéristiques des clients et les tendances de churn.
3. Prédire le Churn : Dans l’onglet de prédiction, entrez le numéro d’un client pour obtenir la probabilité de churn associée et savoir s’il est à risque ou non.

	    Structure du Code

- `app.py` : Contient le code de l’API Flask pour gérer les requêtes de prédiction.
- `interface.py` : Fichier Streamlit pour l’interface utilisateur, comprenant les onglets pour l’exploration des données et la prédiction du churn.
- `model/` : Dossier contenant le modèle de machine learning (RandomForest) ainsi que les scripts de prétraitement et de sauvegarde.
- `data/` : Dossier où sont stockées les données clients utilisées pour l’entraînement et les tests.

	  Technologies Utilisées

- Python : Langage principal pour le développement de l’application.
- Flask : Framework léger pour construire l’API backend.
- Streamlit : Bibliothèque pour créer l’interface utilisateur interactive.
- Scikit-Learn : Utilisé pour le modèle RandomForest et le prétraitement des données.
- Pandas & NumPy : Pour la manipulation et l’analyse des données.
- SMOTE (imbalanced-learn) : Pour équilibrer les classes en ajustant la distribution des données.

	  Auteurs et Contributeurs

Développé par Elias Pianko Hadjira Riad.  
