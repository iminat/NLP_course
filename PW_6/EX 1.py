from gensim.models import Word2Vec

# Define your collection of documents
documents = [
    ["I", "like", "apples"],
    ["I", "like", "bananas"],
    ["I", "like", "oranges"],
    ["I", "like", "fruits"]
]

# Train word vectors
model = Word2Vec(documents, vector_size=100, window=5, min_count=1, workers=4)

# Test word similarity
similarity = model.wv.similarity('apples', 'bananas')
print(f"Similarity between 'apples' and 'bananas': {similarity}")

