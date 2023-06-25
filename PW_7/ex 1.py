import pandas as pd
from textblob import TextBlob
import googlemaps

# Function to extract reviews from Google Maps using Google Maps API
def get_reviews(api_key, place_id, num_reviews):
    gmaps = googlemaps.Client(key=api_key)
    reviews = gmaps.place(place_id, fields=["review"])[0]['review']
    return [review['text'] for review in reviews[:num_reviews]]

# Function to perform sentiment analysis using TextBlob
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiment = 1 if polarity >= 0 else 0
    return polarity, subjectivity, sentiment

# Sample places and their corresponding Google Maps place IDs
places = {
    "Hotel": "your_hotel_place_id",
    "Cafe": "your_cafe_place_id",
    "Restaurant": "your_restaurant_place_id"
}

# Specify the number of reviews to extract for each place
num_reviews = 20

# API key for Google Maps
api_key = "your_google_maps_api_key"

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=["Review", "Polarity", "Subjectivity", "Sentiment"])

# Extract reviews, perform sentiment analysis, and populate the DataFrame
for place, place_id in places.items():
    reviews = get_reviews(api_key, place_id, num_reviews)
    for review in reviews:
        polarity, subjectivity, sentiment = perform_sentiment_analysis(review)
        df = df.append({"Review": review, "Polarity": polarity, "Subjectivity": subjectivity, "Sentiment": sentiment},
                       ignore_index=True)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("sentiment_analysis_results.csv", index=False)

# Create three output files with "Review" and "Sentiment" columns
for place, place_id in places.items():
    place_df = df[df["Review"].str.contains(place, case=False)]
    place_df[["Review", "Sentiment"]].to_csv(f"{place.lower()}_sentiment.csv", index=False)
