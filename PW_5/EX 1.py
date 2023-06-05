import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import networkx as nx
from gensim.models import KeyedVectors

# Step 1: Load articles from CSV file
df = pd.read_csv('articles.csv')

# Step 2: Load GloVe model
glove_model = KeyedVectors.load_word2vec_format('glove_model.txt', binary=False)

# Step 3: Read articles with data
articles = df['article'].tolist()

# Step 4: Clean text of articles (assuming you have a function called clean_text)
cleaned_articles = [clean_text(article) for article in articles]

# Step 5: Calculate similarity matrix for each article
vectorizer = CountVectorizer().fit_transform(cleaned_articles)
similarity_matrix = cosine_similarity(vectorizer)

# Step 6: Compute graph with networkx library
graph = nx.from_numpy_array(similarity_matrix)

# Step 7: Rank graph and obtain summary for articles
scores = nx.pagerank(graph)
summary_size = 3  # Number of sentences to include in the summary

# Sort the sentences by their scores in descending order
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(articles)), reverse=True)

# Extract the top sentences to form the summary
summary_sentences = [sentence for _, sentence in ranked_sentences[:summary_size]]

# Print the summary
print("Summary:")
for sentence in summary_sentences:
    print("- " + sentence)