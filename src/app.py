from flask import Flask
import joblib
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

# For Flask
# model = joblib.load("../models/lr_model.pkl")
# vectorizer = joblib.load("../models/vectorizer.pkl")

#For Docker
model = joblib.load("models/lr_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def applySA(inputedVal):
    input = vectorizer.transform([inputedVal])
    results = model.predict(input)[0]
    return results


@app.route('/')
def my_form():
    return render_template('homepage.html')

@app.route('/', methods=['POST', 'GET'])
def sentiment_analysis():

    if request.method == 'POST':
        print(request.form['review'])
        inputSentiment = request.form['review']
        sentiment = applySA(inputSentiment)
        return render_template('sentimentAnalysis.html', finalResults = sentiment)

if __name__ == '__main__':
    app.run(port=5000, debug=True) # for Docker add the parameter : host="0.0.0.0"
