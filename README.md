# NLP_Project

## Contexte :

Ce projet s'inscrit dans le cadre de la formation donnée par Simplon de développeur en intelligence articielle (Ecole IA by Microsoft).  
Il vise développer un outil d'analyse de texte dans le cadre d'un journal intime numérique utilisé par un psychologue pour ses patients. L'objectif est d'analyser les écrits des patients afin d'aider le psychologue dans son travail, sans avoir à lire chaque texte individuellement. Le projet utilise des techniques de traitement automatique du langage naturel (NLP) pour extraire des informations pertinentes des textes.  

## Etapes du projet

Le projet se découpe en 4 étapes :  
- partie 1 : l'analyse des données, le pré-traitement (avec Spacy) et l'implémentation d'un modèle.
- partie 2 : le stockage des données avec Elastic Search.
- partie 3: l'utilisation de Hugging Face.
- partie 4 : la création d'une application de suivi.

## Arborescence des fichiers : 

- *data/Emotion_final.csv* : contient le [dataset](https://www.kaggle.com/datasets/ishantjuyal/emotions-in-text) utilisé pour faire nos analyses et entrainer le modèle.

- *partie_1.ipynb* : contient le code et les étapes de l'analyse, y compris le pré-traitement des données, la création des modèles et l'évaluation des performances.

- *partie_2.ipynb* : contient la méthode pour créer un container à partir de l'image Docker offcielle d'Elasticsearch, puis la réalisation d'un mapping d'index de notes et l'import des données (utilisation de la librairie Faker) et enfin une partie où l'on requête la base de donnée pour conduire différentes analyses.

- *requirements.txt* spécifie les dépendances nécessaires pour exécuter le code du projet.

## Requirements  

Les dépendances nécessaires pour exécuter le code du projet sont répertoriées dans le fichier *requirements.txt*. Vous pouvez les installer en exécutant la commande suivante : `pip install -r requirements.txt`

## Auteurs 

Myriam Le Bihan et Ahmad Darwiche  
