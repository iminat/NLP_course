import nltk

# Tokenize the sentence
text = "George Bool is an English mathematician, philosopher and logician"
from nltk.tokenize import word_tokenize
word_tokens = word_tokenize(text)
print(word_tokens)

# Perform PoS tagging
pos_tags = nltk.pos_tag(word_tokens)

# Print the pos tags
print(pos_tags)


import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
pos_tags = [(token.text, token.pos_) for token in doc]
print(pos_tags)