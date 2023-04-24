import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize

sentence = "Sam and Anna played tennis in the park while Tom watched from the window, cheering them on"
tokens = word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
named_entities = ne_chunk(tagged, binary=True)
print(named_entities)

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentence)
for ent in doc.ents:
    print(ent.text, ent.label_)