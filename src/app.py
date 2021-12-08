from flask import Flask
import joblib

# model = joblib.load("C://Users/alexa/Desktop/dataengineering2_project/models/lr_model.pkl")
model = joblib.load("../models/lr_model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

def sentiment_analysis(sentence):
    input = vectorizer.transform([sentence])
    result = model.predict(input)[0]

    print(result)


resultat = sentiment_analysis("I am not happy")
