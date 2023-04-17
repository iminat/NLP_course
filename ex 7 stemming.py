import nltk

# Define a list of words
words = ['climbing', 'climbs', 'climbers', 'climbed', 'studying', 'studies', 'is', 'am']

# NLTK Stemming
porter = nltk.PorterStemmer()
nltk_stems = []
for word in words:
    stem = porter.stem(word)
    nltk_stems.append(stem)
print("NLTK Stemming:", nltk_stems)

