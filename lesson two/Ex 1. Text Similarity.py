from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define three pairs of sentences
sentences = [
("I sat on the bench", "The cat sat on the floor"),
("The naughty boy jumps over the lazy cat.", "The lazy cat is jumped over by the naughty boy"),
("This is first sentence", "This is second one")
]

# Define lemmatizer and stemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Define function for lemmatizing and stemming words in a sentence
def lemmatize_stem(sentence):
    words = word_tokenize(sentence.lower())
    return [stemmer.stem(lemmatizer.lemmatize(word)) for word in words]

# Define TfidfVectorizer and fit it on the sentences
vectorizer = TfidfVectorizer(tokenizer=lemmatize_stem)
vectors = vectorizer.fit_transform(sentences)

# Calculate cosine similarity between the sentences
cosine_similarities = cosine_similarity(vectors)

# Calculate Jaccard similarity between the sentences
jaccard_similarities = []
for i in range(len(sentences)):
    sentence1_words = set(lemmatize_stem(sentences[i][0]))
    sentence2_words = set(lemmatize_stem(sentences[i][1]))
    intersection = sentence1_words.intersection(sentence2_words)
    union = sentence1_words.union(sentence2_words)
    jaccard_similarities.append(len(intersection) / len(union))

# Print the results
for i in range(len(sentences)):
    print(f"Sentence pair {i+1}:")
    print(f"Cosine similarity: {cosine_similarities[i][1]}")
    print(f"Jaccard similarity: {jaccard_similarities[i]}")
    print()

#In this code, I first define three pairs of sentences.
# Then, define a lemmatizer and stemmer using NLTK's WordNetLemmatizer and PorterStemmer classes.
# I also define a function called lemmatize_stem that takes a sentence, tokenizes it using NLTK's word_tokenize function,
# lemmatizes each word using the WordNetLemmatizer, and then stems each word using the PorterStemmer.

#Next, I define a TfidfVectorizer and fit it on the sentences using the fit_transform method.
# This generates a matrix of TF-IDF vectors for each sentence.then calculate the cosine similarity between each pair of
# sentences using the cosine_similarity function from scikit-learn.

#Finally, calculate the Jaccard similarity between each pair of sentences by lemmatizing and stemming each word in
# both sentences, finding the intersection and union of the resulting sets of words, and calculating the Jaccard
# similarity as the ratio of the intersection size to the union size.