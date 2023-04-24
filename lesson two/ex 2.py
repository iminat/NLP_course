import nltk
from textblob import TextBlob

text = "John you should correct your code in line 68."

# Custom function to extract n-grams
def extract_ngrams(text, n):
    words = text.split()
    ngrams = []
    for i in range(len(words)-n+1):
        ngram = tuple(words[i:i+n])
        ngrams.append(ngram)
        return ngrams

# Extract trigrams using custom function
trigrams = extract_ngrams(text, 3)
print(trigrams)

# Extract trigrams using NLTK
tokens = nltk.word_tokenize(text)
trigrams = list(nltk.ngrams(tokens, 3))
print(trigrams)

# Extract trigrams using TextBlob
blob = TextBlob(text)
trigrams = blob.ngrams(n=3)
print(trigrams)

#Explanation:

#The custom function extract_ngrams(text, n) takes a text and an integer n as input, splits the text into words,
#and returns a list of tuples representing n-grams.
#nltk.word_tokenize(text) tokenizes the text into a list of words using the NLTK tokenizer.
#nltk.ngrams(tokens, 3) takes a list of tokens and an integer n as input, and returns a list of n-grams.
#TextBlob(text).ngrams(n=3) creates a TextBlob object from the text and extracts n-grams using the ngrams() method.