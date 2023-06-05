import pandas as pd
from gensim.summarization import summarize

# Step 1: Load articles from CSV file
df = pd.read_csv('sample4.csv')

# Step 2: Read articles with data
articles = df['article'].tolist()

# Step 3: Apply TextRank algorithm to articles
summary_size = 3  # Number of sentences to include in the summary

print("Summary:")
for article in articles:
    # Apply TextRank algorithm using gensim's summarize function
    summary = summarize(article, word_count=summary_size, split=True)

    # Print the summary
    for sentence in summary:
        print("- " + sentence)
    print()