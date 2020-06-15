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

@app.route("/predict/<type>", methods=["GET", "POST"])
def getPrediction():
	def predictAsma():
		asma = joblib.load('./models/asma.pkl')
		asma.predict()
	
	def predictCardiovascular():
		cardiovascular = joblib.load('./models/cardiovascular.pkl')
	
	def predictDiabetes():
		diabetes = joblib.load('./models/diabetes.pkl')
	
	def predictEmbarazo():
		embarazo = joblib.load('./models/embarazo.pkl')
	
	def predictEpoc():
		epoc = joblib.load('./models/epoc.pkl')
	
	def predictHipertension():
		hipertension = joblib.load('./models/hipertension.pkl')
	
	def predictInmusupr():
		inmusupr = joblib.load('./models/inmusupr.pkl')
	
	def predictNeumonia():
		neumonia = joblib.load('./models/neumonia.pkl')
	
	def predictObesidad():
		obesidad = joblib.load('./models/obesidad.pkl')
	
	def predictRenal():
		renal = joblib.load('./models/renal.pkl')
	
	def predictTabaquismo():
		tabaquismo = joblib.load('./models/tabaquismo.pkl')

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

	return render_template("")
	

if __name__ == '__main__':
	app.run()