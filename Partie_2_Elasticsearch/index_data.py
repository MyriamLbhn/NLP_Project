import csv
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import numpy as np
from faker import Faker
from elasticsearch import Elasticsearch
import sys
sys.path.append('Partie_1_Analyse')
import pickle
import requests


# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
index = 'notes'  
# Fonction pour supprimer les documents
def delete_documents(index):
    url = f'http://localhost:9200/{index}/_delete_by_query'
    query = {
        "query": {
            "match_all": {}
        }
    }
    response = requests.post(url, json=query)

    if response.status_code == 200:
        print("Suppression des documents terminée.")
    else:
        print("Erreur lors de la suppression des documents.")

# Utilisation de la fonction
delete_documents(index)

# Charger le pipeline pré-entraîné
with open('Partie_1_Analyse/pipeline/nlp-pipeline-linearsvc.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Instanciation de Faker
fake = Faker()

# Liste de patients
patients = []
patient_left_values = []
for _ in range(200):
    patient_lastname, patient_firstname = fake.last_name(), fake.first_name()
    patients.append((patient_lastname, patient_firstname))
    patient_left_values.append(fake.boolean())

# Chemin vers le fichier CSV
csv_file = 'Partie_1_Analyse/data/Emotion_final.csv'

# Lecture du fichier CSV et indexation des données
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    count = 0  # Compteur de documents indexés

    for i, row in enumerate(reader):
        # Sélectionner le texte de la ligne
        text = row['Text']

        # Prétraitement, vectorisation et prédiction avec le pipeline
        emotion = pipeline.predict([text])[0]
        decision = pipeline.decision_function([text])[0]
        confidence = max(1 / (1 + np.exp(-decision)))

        # Sélectionner le patient correspondant
        patient_lastname, patient_firstname = patients[i % len(patients)]

        # Récupérer la valeur unique de "patient_left" pour le patient actuel
        patient_left = patient_left_values[i % len(patient_left_values)]

        # Générer une date aléatoire jusqu'à 2 ans maximum
        max_date = datetime.now() - timedelta(days=365 * 2)
        date = fake.date_between(start_date='-2y', end_date='today')

        # Créer le document à indexer
        doc = {
            'patient_lastname': patient_lastname,
            'patient_firstname': patient_firstname,
            'text': text,
            'date': date,
            'patient_left': patient_left,
            'emotion': emotion,
            'confidence': confidence
        }

        # Indexation du document dans Elasticsearch
        es.index(index=index, document=doc)
        
        count += 1
        if count % 100 == 0:
            print(f"Nombre total de documents indexés : {count}")        

print(f"Indexation terminée. Nombre total de documents indexés : {count}")
