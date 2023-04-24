from collections import Counter
import re

# Define the input text
text = "The naughty boy jumps over the lazy cat. The cat meows but the naughty boy doesn't care."

# Tokenize the text into words
tokens = re.findall(r'\w+', text)

# Count the frequency of each term
term_counts = Counter(tokens)

# Print the 10 most frequent terms
for term, count in term_counts.most_common(10):
    print(term, count)

#This code first uses the re module to tokenize the text into individual words
#We then use the Counter class from the collections module to count the frequency of each term in the text.
#The resulting term_counts object is a dictionary-like object where each key is a unique term and each value is the frequency count for that term.
#Finally, we use the most_common() method of the Counter object to return a list of the 10 most frequent terms in the text, along with their respective frequency counts.
# We use a for loop to iterate through this list and print each term and count.