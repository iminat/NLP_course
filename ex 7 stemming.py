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

import spacy

nlp = spacy.load("en_core_web_sm")
for i in words:
    doc = nlp(i)
print(i, ":", doc[0].lemma_)

