import nltk
import spacy

words = ['climbing', 'climbs', 'climbers', 'climbed', 'studying', 'studies', 'is', 'am']

lemmatizer = nltk.WordNetLemmatizer()
nltk_lemmas = []
for word in words:
    lemma = lemmatizer.lemmatize(word)
    nltk_lemmas.append(lemma)
print("NLTK Lemmatization:", nltk_lemmas)

