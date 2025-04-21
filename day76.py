import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample intents
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye", "take care"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "that's helpful"],
        "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
    },
    "age": {
        "patterns": ["how old are you?", "what is your age?"],
        "responses": ["I'm timeless!", "I exist beyond time."]
    },
    "name": {
        "patterns": ["what is your name?", "who are you?"],
        "responses": ["I'm your friendly chatbot!", "You can call me ChatBot."]
    }
}

# Prepare training data
X = []
y = []

for intent, data in intents.items():
    for pattern in data["patterns"]:
        X.append(pattern)
        y.append(intent)

# Vectorize text
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train classifier
model = MultinomialNB()
model.fit(X_vectorized, y)

# Chat function
def chatbot():
    print("Chatbot: Hello! Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Bye! Have a great day.")
            break

        user_vector = vectorizer.transform([user_input])
        intent_pred = model.predict(user_vector)[0]
        response = random.choice(intents[intent_pred]["responses"])
        print("Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()
