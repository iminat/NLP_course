from keras.preprocessing.text import text_to_word_sequence
from textblob import TextBlob

text = "John you should correct your code in line 68."

# Tokenize text using Keras
tokens = text_to_word_sequence(text)
print(tokens)

# Tokenize text using TextBlob
blob = TextBlob(text)
tokens = blob.words
print(tokens)

#Explanation:

#text_to_word_sequence(text) is a method from the Keras package that takes a string as input
#and returns a list of words in the string, where each word has been lowercased and punctuation has been removed.
#TextBlob(text).words is a method from the TextBlob package that takes a string as input and returns a list of words in the string,
#where each word has been tokenized and normalized.