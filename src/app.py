import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
    # model = joblib.load("C://Users/alexa/Desktop/dataengineering2_project/models/lr_model.pkl")
    model = joblib.load("../models/lr_model.pkl")
    vectorizer = joblib.load("../models/vectorizer.pkl")

    def sentiment_analysis(sentence):
        input = vectorizer.transform([sentence])
        result = model.predict(input)[0]

        return result
    return(render_template('index.html', variable=result))



