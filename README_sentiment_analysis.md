Sentiment Analysis Programme

This Python programme performs sentiment analysis on a dataset of Amazon consumer reviews using the TextBlob library and spaCy.

Installation
Before running the programme, make sure you have the following Python libraries installed:

pandas
spacy
textblob

You can install these libraries using pip:
pip install pandas spacy textblob

Additionally, you'll need to download the English language model for spaCy:
python -m spacy download en_core_web_md

Usage
1. Import Libraries:
Import the required libraries at the beginning of your Python script:

import pandas as pd
import spacy
from textblob import TextBlob

2. Load Data:
Load the dataset containing Amazon consumer reviews:

data = pd.read_csv("path/to/dataset.csv")

3. Perform Sentiment Analysis:
Define a function to perform sentiment analysis on each review:

def analyse_sentiment(review):
    analysis = TextBlob(str(review))
    sentiment = analysis.sentiment.polarity
    print(f"Review: {review}")
    print(f"Sentiment Polarity: {sentiment}")
    return sentiment
    
4. Apply Sentiment Analysis:
Apply the sentiment analysis function to each review in the dataset:

data['sentiment'] = data['reviews.text'].dropna().apply(analyse_sentiment)

5. Calculate Mean Polarity:
Calculate the mean polarity of the sentiment scores:

mean_polarity = data['sentiment'].mean()
print(f"Mean Polarity: {mean_polarity}")

6. Calculate Semantic Similarity:
Choose two indices of the reviews to compare and calculate the semantic similarity between them using spaCy:

index1 = 67  # Index of the first review
index2 = 120 # Index of the second review

review1 = data['reviews.text'].iloc[index1]
review2 = data['reviews.text'].iloc[index2]

doc1 = nlp(review1)
doc2 = nlp(review2)

similarity = doc1.similarity(doc2)
print(f"Semantic similarity between review {index1} and review {index2}: {similarity}")

Notes

1. Replace "path/to/dataset.csv" with the path to your dataset file.
2. Ensure that the dataset contains a column named 'reviews.text' containing the reviews.
3. This programme utilises the English language model (en_core_web_md) provided by spaCy. Ensure that it is downloaded before running the programme.

Credits
This programme was written by Maïa Kalina.
It utilises the TextBlob library for sentiment analysis and the spaCy library for semantic similarity calculation.