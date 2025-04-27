import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data (only once)
nltk.download('punkt')
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Sample chatbot pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there!", "Hey! How's it going?"]
    ],
    [
        r"what is your name\??",
        ["I'm a chatbot created for the internship task!", "I don’t have a name, but I’m here to help."]
    ],
    [
        r"how are you\??",
        ["I'm just a bunch of code, but I'm functioning great!", "Doing great! Ready to assist you."]
    ],
    [
        r"what can you do\??",
        ["I can chat with you, answer questions, and show simple NLP capabilities.", "I respond to basic queries and can help with information."]
    ],
    [
        r"(.*) your creator\??",
        ["I was created by an intern using Python and NLTK!", "A human programmed me during their internship."]
    ],
    [
        r"tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!"]
    ],
    [
        r"what's the weather like\??",
        ["I can't check the weather right now, but you can use a weather app or website!", "I recommend checking a reliable weather service for the latest updates."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you soon!", "Take care!"]
    ],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Function to analyze sentiment
def analyze_sentiment(user_input):
    sentiment_score = sia.polarity_scores(user_input)
    if sentiment_score['compound'] >= 0.05:
        return "I'm glad to hear you're feeling positive!"
    elif sentiment_score['compound'] <= -0.05:
        return "I'm sorry to hear that. If you want to talk about it, I'm here."
    else:
        return "I see you're feeling neutral. How can I assist you?"

# Start chat
print("Hi! I'm your internship chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        # Analyze sentiment and respond
        sentiment_response = analyze_sentiment(user_input)
        print("Chatbot:", sentiment_response)
        chatbot.respond(user_input)
