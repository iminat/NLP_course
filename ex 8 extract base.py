import nltk

words = ['jumping', 'climbs', 'climbers', 'climbed', 'studying', 'studies', 'is', 'am']

lemmatizer = nltk.WordNetLemmatizer()
nltk_lemmas = []
for word in words:
    lemma = lemmatizer.lemmatize(word)
    nltk_lemmas.append(lemma)
print("NLTK Lemmatization:", nltk_lemmas)

import spacy

nlp = spacy.load("en_core_web_sm")
for i in words:
    doc = nlp(i)
print(i, ":", doc[0].lemma_)

