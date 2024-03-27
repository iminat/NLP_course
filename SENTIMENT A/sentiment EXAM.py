import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the dataset
wine_reviews = pd.read_json('winemag-data-130k-v2.json')

# Tokenize the descriptions
wine_reviews['tokens'] = wine_reviews['description'].apply(word_tokenize)

# Remove stopwords
stop_words = set(stopwords.words('english'))
wine_reviews['filtered_tokens'] = wine_reviews['tokens'].apply(lambda tokens: [word for word in tokens if word.lower() not in stop_words])

# Define positive and negative word lists
positive_words = set(['good', 'great', 'excellent', 'wonderful', 'amazing', 'love', 'like', 'best', 'fantastic'])
negative_words = set(['bad', 'poor', 'terrible', 'awful', 'horrible', 'dislike', 'hate'])

# Function to calculate sentiment score
def calculate_sentiment_score(tokens):
    positive_score = sum(1 for token in tokens if token.lower() in positive_words)
    negative_score = sum(1 for token in tokens if token.lower() in negative_words)
    return positive_score - negative_score

# Apply sentiment analysis to descriptions
wine_reviews['sentiment_score'] = wine_reviews['filtered_tokens'].apply(calculate_sentiment_score)

# Assign sentiment label based on sentiment score
wine_reviews['sentiment'] = wine_reviews['sentiment_score'].apply(lambda score: 'Positive' if score > 0 else ('Negative' if score < 0 else 'Neutral'))


# Print the sentiment analysis for each review
pd.set_option('display.max_rows', None)
print(wine_reviews[['description', 'sentiment']])
