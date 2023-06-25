import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset from Ex. 1
df = pd.read_csv("sentiment_analysis_results.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df["Review"], df["Sentiment"], test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the training data and transform the training data
X_train_vectorized = vectorizer.fit_transform(X_train)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Evaluate the model on the testing data
X_test_vectorized = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Example sentences to test the model
examples = [
    "This hotel exceeded my expectations. The staff was friendly and the room was clean.",
    "The cafe had terrible service and the coffee was awful.",
    "I had a fantastic dining experience at the restaurant. The food was delicious and the atmosphere was cozy."
]

# Vectorize the example sentences and make predictions
example_vectorized = vectorizer.transform(examples)
example_predictions = model.predict(example_vectorized)

# Display the example sentences and their predicted sentiments
for example, prediction in zip(examples, example_predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Sentence: {example}")
    print(f"Sentiment: {sentiment}")
    print()

# Examples where the model may give negative results
negative_examples = [
    "The hotel room was dirty and the staff was rude.",
    "The cafe served me a burnt sandwich and it took forever to get my order.",
    "The restaurant had a bad smell and the food tasted terrible."
]

# Vectorize the negative examples and make predictions
negative_vectorized = vectorizer.transform(negative_examples)
negative_predictions = model.predict(negative_vectorized)

# Display the negative examples and their predicted sentiments
for example, prediction in zip(negative_examples, negative_predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Sentence: {example}")
    print(f"Sentiment: {sentiment}")
    print()
