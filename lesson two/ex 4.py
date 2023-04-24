import nltk
from nltk.tokenize import TweetTokenizer, MWETokenizer, RegexpTokenizer, WhitespaceTokenizer, WordPunctTokenizer

text = "Look! John, you should correct your code in line 68 and leave comment using #."

# Tokenize text using TweetTokenizer
tokenizer = TweetTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)

# Tokenize text using RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
print(tokens)

# Tokenize text using WhitespaceTokenizer
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)

# Tokenize text using WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)