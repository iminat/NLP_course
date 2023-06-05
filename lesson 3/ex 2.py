from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
categories = ['sci.med', 'comp.graphics', 'rec.autos']  # Choose desired categories
newsgroups = fetch_20newsgroups(subset='all', categories=categories)

# Preprocess the text data and create document vectors
vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(newsgroups.data)

# Perform k-means clustering with different numbers of clusters
max_clusters = 10  # Maximum number of clusters to try
inertia = []
for k in range(1, max_clusters+1):
    clustering = KMeans(n_clusters=k)
    clustering.fit(document_vectors)
    inertia.append(clustering.inertia_)

# Plot the elbow curve to determine the optimal number of clusters
plt.plot(range(1, max_clusters+1), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Curve')
plt.show()

# Determine the optimal number of clusters
optimal_clusters = np.argmin(inertia) + 1
print(f"Optimal number of clusters: {optimal_clusters}")

# Perform k-means clustering with the optimal number of clusters
clustering = KMeans(n_clusters=optimal_clusters)
clusters = clustering.fit_predict(document_vectors)

# Compare clusters with actual categories
if newsgroups.target is not None:
    for i in range(len(newsgroups.target)):
        print(f"Document {i+1}: Predicted Cluster {clusters[i]}, Actual Category {newsgroups.target[i]}")