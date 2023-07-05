from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from preprocessing import TextProcessor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle


df = pd.read_csv('analyse/data/Emotion_final.csv')

# Création du pipeline
nlp_pipeline = Pipeline([
    ('preprocessor', TextProcessor()),
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LinearSVC())
])

X = df['Text']
y = df['Emotion']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nlp_pipeline.fit(X_train, y_train)

y_pred = nlp_pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

with open('analyse/pipeline/nlp-pipeline-linearsvc.pkl', 'wb') as file:
    pickle.dump(nlp_pipeline, file)