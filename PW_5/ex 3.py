import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

# Step 1: Create and analyze three different texts
text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac ligula at justo congue viverra. Nulla facilisi. Aenean id sem quis mauris ultrices aliquam. Integer finibus feugiat nunc ac fringilla. Morbi pellentesque semper neque id feugiat. Etiam vitae placerat mauris. Sed rutrum tortor vel justo efficitur, in fermentum mi eleifend."
text2 = "Suspendisse posuere, massa id feugiat suscipit, enim sem ultrices mi, et vestibulum sem mauris nec turpis. Donec dignissim est in libero convallis, eu tincidunt velit feugiat. In finibus nulla velit, id commodo purus placerat et. Vestibulum id tortor eget dui dignissim lobortis id in ipsum. Etiam vitae ante risus."
text3 = "Phasellus vitae interdum neque. Proin sit amet ligula eget ligula tristique gravida vitae ut turpis. Sed consequat enim ipsum, ac mattis odio condimentum sit amet. Maecenas finibus, purus vitae pulvinar malesuada, eros turpis feugiat nisi, at sollicitudin ex risus non purus."

texts = [text1, text2, text3]

# Step 2: Calculate word frequencies
def calculate_word_frequencies(text):
    words = word_tokenize(text.lower())
    fdist = FreqDist(words)
    return {word: freq / fdist.most_common(1)[0][1] for word, freq in fdist.items()}

# Step 3: Drop uncommon or common words based on proportions
def filter_words(word_frequencies, min_proportion, max_proportion):
    return {word: freq for word, freq in word_frequencies.items() if min_proportion <= freq <= max_proportion}

# Step 4: Score frequencies of words and summarize the text
def summarize_text(text, top_sentences):
    word_frequencies = calculate_word_frequencies(text)
    filtered_word_frequencies = filter_words(word_frequencies, 0.1, 0.9)
    sentence_scores = {sentence: sum(filtered_word_frequencies.get(word, 0) for word in word_tokenize(sentence.lower()))
                       for sentence in sent_tokenize(text)}
    top_sentences = nlargest(top_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join(top_sentences)

# Summarize the texts
num_top_sentences = 2
for text in texts:
    summary = summarize_text(text, num_top_sentences)
    print("Summary:")
    print(summary)
    print()