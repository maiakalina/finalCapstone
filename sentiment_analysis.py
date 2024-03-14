import pandas as pd
import spacy
from textblob import TextBlob

# Load the 'en_core_web_sm' model
nlp = spacy.load('en_core_web_md')

# Load the dataset
data = pd.read_csv("/Users/maiiakalina/Desktop/task 21/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv")

# Select the 'reviews.text' column
reviews_data = data['reviews.text']

# Clean data
reviews_data = reviews_data.dropna()

# Perform sentiment analysis
def analyse_sentiment(review):
    analysis = TextBlob(str(review))
    sentiment = analysis.sentiment.polarity
    print(f"Review: {review}")
    print(f"Sentiment Polarity: {sentiment}")
    return sentiment

# Apply sentiment analysis to each review
data['sentiment'] = reviews_data.apply(analyse_sentiment)

# Calculate mean polarity
mean_polarity = data['sentiment'].mean()

# Output the mean polarity result
print(f"Mean Polarity: {mean_polarity}")

# Choose two indices of the reviews to compare
index1 = 67  # Index of the first review
index2 = 120 # Index of the second review

# Select the two reviews
review1 = reviews_data.iloc[index1]
review2 = reviews_data.iloc[index2]

# Process the reviews using spaCy
doc1 = nlp(review1)
doc2 = nlp(review2)

# Calculate semantic similarity between the processed reviews
similarity = doc1.similarity(doc2)

# Output the similarity
print(f"Semantic similarity between review {index1} and review {index2}: {similarity}")