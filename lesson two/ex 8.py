import re

# Define the input text
text = "Who has done it and when?"

# Count the number of words in the text
num_words = len(re.findall(r'\w+', text))

# Check if the text contains any "wh-" words
wh_words = re.findall(r'\b(who|what|when|where|why|how)\b', text)

print("Number of words:", num_words)
print("Contains wh- words:", len(wh_words) > 0)


#Explanation
#This code uses the re module to perform regular expression matching.
#I first use a regular expression pattern (r'\w+') to match all contiguous sequences of alphanumeric characters in the text.
# then count the number of matches to determine the number of words.

#Next, I use a similar regular expression pattern to match any "wh-" words that appear as whole words in the text.
# use the \b metacharacter to match word boundaries and the | character to specify multiple alternative words.
# then check if the resulting list of matches is non-empty to determine if the text contains any "wh-" words.