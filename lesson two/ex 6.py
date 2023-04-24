import nltk
from nltk.stem import PorterStemmer

text = "John is correcting his code in line 68."

# Define stemmer to use the Porter algorithm
stemmer = PorterStemmer()

# Apply stemmer to each word in the text
tokens = nltk.word_tokenize(text)
for token in tokens:
    stemmed_token = stemmer.stem(token)
    stemmed_tokens.append(stemmed_token)

# Print original and stemmed tokens
print(tokens)
print(stemmed_tokens)

#Explanation:

#PorterStemmer() is a stemmer from the NLTK package that implements the Porter stemming algorithm, which is a widely used algorithm for English stemming.
#stemmer.stem(token) is a method of the stemmer object that takes a token as input and returns the stemmed version of the token.