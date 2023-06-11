from gensim.models import KeyedVectors
import matplotlib.pyplot as plt

# Load pre-trained GloVe word vectors
glove_model = KeyedVectors.load_word2vec_format('glove.6B.50d.txt', binary=False)

# Access word vectors
vector_apples = glove_model['apples']
vector_bananas = glove_model['bananas']

# Display image representation
plt.figure(figsize=(8, 6))
plt.scatter(vector_apples[0], vector_apples[1], color='red', label='apples')
plt.scatter(vector_bananas[0], vector_bananas[1], color='blue', label='bananas')
plt.legend()
plt.title('Word Vectors: Apples and Bananas')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
