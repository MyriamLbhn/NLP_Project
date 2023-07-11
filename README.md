# NLP_Project

## Contexte :

Ce projet de 2 semaines s'inscrit dans le cadre de la formation donnée par Simplon de développeur en intelligence articielle (Ecole IA by Microsoft).  
Il vise développer un outil d'analyse de texte dans le cadre d'un journal intime numérique utilisé par un psychologue pour ses patients. L'objectif est d'analyser les écrits des patients afin d'aider le psychologue dans son travail, sans avoir à lire chaque texte individuellement. Le projet utilise des techniques de traitement automatique du langage naturel (NLP) pour extraire des informations pertinentes des textes.  

Le projet se découpe en 4 étapes :  
- partie 1 : l'analyse des données, le pré-traitement (avec Spacy) et l'implémentation d'un modèle.
- partie 2 : le stockage des données avec Elastic Search.
- partie 3: l'utilisation de Hugging Face.
- partie 4 : la création d'une application de suivi.

## Partie 1 : Analyse

Cette partie consiste a analyser le dataset. On explorera aussi les différentes méthodes de pré-traitements (Bag of words et TF-IDF) en gérant les étapes de tokenisation, de gestion de la ponctuation, des émojis, des stopwords, de lemmatisation ou de steaming puis on implémente un modèle de machine learning de scikit learn.  

- *data/Emotion_final.csv* : contient le [dataset](https://www.kaggle.com/datasets/ishantjuyal/emotions-in-text) utilisé pour faire nos analyses et entrainer le modèle.

- *partie_1_analyse.ipynb* : contient le code et les étapes de l'analyse, y compris le pré-traitement des données, la création des modèles et l'évaluation des performances.

- *preprocessing.py* : définition de la classe TextProcessor pour gérer le traitement des stopwords, de la ponctuation et de la lemmatisation

- *tf-idf-pipeline.py* : création du pipeline comprenant le prétraitement, la vectorisation et la modelisation, le pipeline est ensuite exporté

- *pipeline/nlp-pipeline.pkl* : pipeline entrainé

## Partie 2 : Elasticsearch

Info : pour exectuer les fichiers bash, il faut les rendre executables, dans le répertoir *bash_commands*, executez la commande `chmod +x nom_du_fichier`, on peut ensuite l'executer avec la commande `./nom_du_fichier`.  

- *partie_2_elasticsearch.ipynb* : 
    - 2.1 : méthode pour créer un conteneur à partir de l'image Docker officielle d'Elasticsearch
        - *bash_commands/set_up_elastic.sh* : commandes bash pour créer un conteneur elastic search  
    - 2.2 : réalisation d'un mapping d'index de notes et l'indexation des données en utilisant le fichier csv, les prédictions du modèle et la librairie Faker  
        - *bash_commands/mapping.sh* : commandes bash pour créer le mapping de l'index
        - *index.py* : script python pour indexer les données

    - 2.3 : requêtes de la base de donnée

- *partie_2_suite.ipynb* :
    - 2.4 : questions théoriques sur le sharding et les pipelines d'ingestion
    
    - 2.5 : proposition d'alternative à la gestion des stopwords directement dans le mapping et à l'intégration du modèle de ML comme pipeline d'ingestion
    - 2.6 : utilisation de Kibana pour se connecter à la bdd elasticsearch et effectuer des requêtes et visualisations   
        - *bash_commands/set_up_kibana.sh* : commandes bash pour créer un conteneur kibana et le connecter à notre conteneur elastic search

## Partie 3 : Hugging Face



## Partie 4 : Application 

Cette partie concerne le développement d'une application sous Django. Elle dispose d'un système d'authentification pour 2 type de rôle : un rôle patient et un rôle psychologue. Il peut y avoir plusieurs psychologues sur l’application. Chaque patient est affilié à un seul psychologue. Les patients peuvent effectuer des règlements en ligne. Toutes ces informations sont stockée dans une base de données Postgré SQL (simulée les informations manquantes avec Faker).  
     
Les patients peuvent écrire des textes, ils ont accès à une barre de recherche pour retrouver leurs textes à partir de mot clé. Ils sont susceptibles de faire des fautes d’orthographe. Ils n’ont pas accès au modèle prédictif.   
Quand les patients ajoutent un texte, le texte est évalué par votre modèle déployé sur Hugging face.   

Les psychologues voient l’humeur moyenne des derniers jours à l’aide d’un snackbar par semaine. Ils peuvent avoir ce graphique au global ou pour un patient. Ils peuvent également rechercher un texte en précisant pour quelle émotion. Les psychologues ont également accès à leur chiffre d'affaires pour chaque semaine.      

## Requirements  

Les dépendances nécessaires pour exécuter le code du projet sont répertoriées dans le fichier *requirements.txt*. Vous pouvez les installer en exécutant la commande suivante : `pip install -r requirements.txt`

## Auteurs 

Myriam Le Bihan et Ahmad Darwiche  