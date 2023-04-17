import nltk

# Tokenize the sentence
text = "The cat sat on the mat near the door."
tokens = nltk.word_tokenize(text)

# Get list of English stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Filter out stopwords
filtered_words = []
for word in text.split():
    if word.lower() not in stopwords:
        filtered_words.append(word)

# Print the filtered sentence
filtered_text = ' '.join(filtered_words)
print(filtered_text)

# Print the list of stopwords
print(stopwords)

