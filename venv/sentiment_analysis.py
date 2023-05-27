import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
text = "I hate this movie! It's not fantastic."
sentiment = analyzer.polarity_scores(text)
print(sentiment)