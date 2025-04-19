from textblob import TextBlob

# Sample text data
sample_texts = [
    "I absolutely love this product! It exceeded all my expectations.",
    "This is the worst service I’ve ever experienced.",
    "It’s okay, not the best but not the worst either."
]

# Analyze each sentence
for i, text in enumerate(sample_texts, 1):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Text {i}: {text}")
    print(f"  - Polarity: {sentiment.polarity}")
    print(f"  - Subjectivity: {sentiment.subjectivity}")
    print(f"  - Sentiment: {'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'}\n")
