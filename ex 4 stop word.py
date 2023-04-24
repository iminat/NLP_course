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

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
stop_words = spacy.lang.en.stop_words.STOP_WORDS
filtered_tokens = [token.text for token in doc if token.text.lower() not in stop_words]
filtered_text = ' '.join(filtered_tokens)
print("Filtered Text:", filtered_text)
print("Stop Words:", stop_words)