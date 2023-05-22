import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

# Load the file document
file_path = 'file_document.txt'
with open(file_path, 'r') as file:
    document = file.read()

# Preprocess the document
document = [document]

# Training dataset (example)
X_train = [
    "This is a positive review",
    "I really enjoyed this movie",
    "The product works well",
    "I had a terrible experience with their customer service",
    "This book is a must-read"
]

y_train = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Positive"
]

# Convert the text data into numerical features
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
document_vectorized = vectorizer.transform(document)

# Logistic Regression classification
logreg_classifier = LogisticRegression()
logreg_classifier.fit(X_train_vectorized, y_train)
logreg_prediction = logreg_classifier.predict(document_vectorized)
print(f"Logistic Regression Prediction: {logreg_prediction}")

# Naïve Bayes classification
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vectorized, y_train)
nb_prediction = nb_classifier.predict(document_vectorized)
print(f"Naïve Bayes Prediction: {nb_prediction}")

# K-Nearest Neighbors classification
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train_vectorized, y_train)
knn_prediction = knn_classifier.predict(document_vectorized)
print(f"KNN Prediction: {knn_prediction}")