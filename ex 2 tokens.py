
text = 'George Bool is an English mathematician, philosopher and logician'
from nltk.tokenize import word_tokenize
word_tokens = word_tokenize(text)
print(word_tokens)

import spacy
nlp = spacy.load("en_core_web_sm")
tokens = []
doc = nlp(text)
for token in doc:
    tokens.append(token.text)
print(tokens)
