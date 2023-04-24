import nltk
from nltk.stem import RegexpStemmer

text = "John is correcting his code in line 68."

# Define stemmer to remove "ing" suffix
stemmer = RegexpStemmer('ing')

# Apply stemmer to each word in the text
tokens = nltk.word_tokenize(text)
stemmed_tokens = []
for token in tokens:
    if token.endswith('ing'):
        stemmed_token = stemmer.stem(token)
        stemmed_tokens.append(stemmed_token)
    else:
        stemmed_tokens.append(token)

# Print original and stemmed tokens
print(tokens)
print(stemmed_tokens)

#Explanation

#For each token, it checks if it ends with 'ing' using the endswith() method.
#If it does, the stemmer object is used to stem the token using the stem() method, and the stemmed token is appended to the list of stemmed_tokens.
#Otherwise, the original token is appended to the list unchanged.
#Finally, the resulting list of stemmed_tokens is returned.