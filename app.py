from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def classify_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "POSITIVE"
    elif polarity < 0:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = classify_sentiment(text)
    return render_template('index.html', text=text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)