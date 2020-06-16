from flask import Flask, render_template, url_for, request, jsonify

import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt

import seaborn as sb
from scipy.stats.stats import pearsonr

import os
import json

from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/illness/", methods=["GET", "POST"])
def getCorrelation():
	if request.method == "POST":
		selected_illness = request.form["illness-select"]
		print(selected_illness)

		return str(selected_illness)

@app.route("/predict/<predict_type>", methods=["GET", "POST"])
def processPrediction(predict_type):
	def predictAsma():
		asma = joblib.load('./models/asma.pkl')
		dataToPredict = request.get_json()
		prediction = asma.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		print(f"prediction from back end: {prediction}")
		return prediction
	
	def predictCardiovascular():
		cardiovascular = joblib.load('./models/cardiovascular.pkl')
		dataToPredict = request.get_json()
		prediction = cardiovascular.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction

	def predictDiabetes():
		diabetes = joblib.load('./models/diabetes.pkl')
		dataToPredict = request.get_json()
		prediction = diabetes.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction

	def predictEmbarazo():
		embarazo = joblib.load('./models/embarazo.pkl')
		dataToPredict = request.get_json()
		prediction = embarazo.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction

	def predictEpoc():
		epoc = joblib.load('./models/epoc.pkl')
		dataToPredict = request.get_json()
		prediction = epoc.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction

	def predictHipertension():
		hipertension = joblib.load('./models/hipertension.pkl')
		dataToPredict = request.get_json()
		prediction = hipertension.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	

	def predictInmusupr():
		inmusupr = joblib.load('./models/inmusupr.pkl')
		dataToPredict = request.get_json()
		prediction = inmusupr.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	
		
	def predictNeumonia():
		neumonia = joblib.load('./models/neumonia.pkl')
		dataToPredict = request.get_json()
		prediction = neumonia.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	

	def predictObesidad():
		obesidad = joblib.load('./models/obesidad.pkl')
		dataToPredict = request.get_json()
		prediction = obesidad.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	

	def predictRenal():
		renal = joblib.load('./models/renal_cronica.pkl')
		dataToPredict = request.get_json()
		prediction = renal.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	

	def predictTabaquismo():
		tabaquismo = joblib.load('./models/tabaquismo.pkl')
		dataToPredict = request.get_json()
		prediction = tabaquismo.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)
		return prediction	

	switch = {
		"asma" : predictAsma(),
		"cardiovascular" : predictCardiovascular(),
		"diabetes" : predictDiabetes(),
		"embarazo" : predictEmbarazo(),
		"epoc" : predictEpoc(),
		"hipertension": predictHipertension(),
		"inmusupr" : predictInmusupr(),
		"neumonia" : predictNeumonia(),
		"obesidad" : predictObesidad(),
		"renal_cronica" : predictRenal(),
		"tabaquismo" : predictTabaquismo()
	}

	prediction = switch.get(predict_type)
	jsonResult = jsonify({ "prediction": prediction })
	return jsonResult




if __name__ == '__main__':
	app.run()