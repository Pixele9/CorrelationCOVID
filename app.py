from flask import Flask, render_template, url_for, request

import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt

import seaborn as sb
from scipy.stats.stats import pearsonr
import os

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
def getPrediction(predict_type):
	def predictAsma():
		asma = joblib.load('./models/asma.pkl')
		dataToPredict = request.get_json()
		prediciton = asma.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		print(f"Prediciton from back end: {prediciton}")
		return prediciton
	
	def predictCardiovascular():
		cardiovascular = joblib.load('./models/cardiovascular.pkl')
		dataToPredict = request.get_json()
		prediciton = cardiovascular.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton

	def predictDiabetes():
		diabetes = joblib.load('./models/diabetes.pkl')
		dataToPredict = request.get_json()
		prediciton = diabetes.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton

	def predictEmbarazo():
		embarazo = joblib.load('./models/embarazo.pkl')
		dataToPredict = request.get_json()
		prediciton = embarazo.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton

	def predictEpoc():
		epoc = joblib.load('./models/epoc.pkl')
		dataToPredict = request.get_json()
		prediciton = epoc.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton

	def predictHipertension():
		hipertension = joblib.load('./models/hipertension.pkl')
		dataToPredict = request.get_json()
		prediciton = hipertension.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	

	def predictInmusupr():
		inmusupr = joblib.load('./models/inmusupr.pkl')
		dataToPredict = request.get_json()
		prediciton = inmusupr.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	
		
	def predictNeumonia():
		neumonia = joblib.load('./models/neumonia.pkl')
		dataToPredict = request.get_json()
		prediciton = neumonia.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	

	def predictObesidad():
		obesidad = joblib.load('./models/obesidad.pkl')
		dataToPredict = request.get_json()
		prediciton = obesidad.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	

	def predictRenal():
		renal = joblib.load('./models/renal_cronica.pkl')
		dataToPredict = request.get_json()
		prediciton = renal.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	

	def predictTabaquismo():
		tabaquismo = joblib.load('./models/tabaquismo.pkl')
		dataToPredict = request.get_json()
		prediciton = tabaquismo.predict([[dataToPredict]])[0][0]
		prediciton = round(prediciton, 0)
		return prediciton	
		
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
		"renal" : predictRenal(),
		"tabaquismo" : predictTabaquismo()
	}

	prediction = switch.get(predict_type)

	return { "prediciton": prediction }
	

if __name__ == '__main__':
	app.run()