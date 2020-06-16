from flask import Flask, render_template, url_for, request, jsonify

import pandas as pd
import numpy as np
import joblib

from scipy.stats.stats import pearsonr
from scipy.stats import variation, tstd
from numpy import mean

import os
import json

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
	pearson = 0
	media = 0
	varianza = 0
	desviacion_estandar = 0

	def predictAsma():
		asma = joblib.load('./models/asma.pkl')
		dataToPredict = request.get_json()
		prediction = asma.predict([[dataToPredict]])[0][0]
		prediction = round(prediction, 0)

		medical_condition = "asma"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

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
	jsonResult = jsonify({ 
		"prediction": prediction, 
		"pearson": pearson, 
		"variance": varianza,
		"std_dev": desviacion_estandar,
		"mean": media
	})
	return jsonResult

def getStats(col_x, file):
	# col x = variable value
	# col y = value to predict
	# filename without extension
	df = pd.read_csv(f"./datasets/{file}.csv")
	x = df[col_x]
	y = df["DEATHS_PER_DAY"]
	pearsonr_coefficient, p_value = pearsonr(x, y)
	variance = variation(df[col_x])
	std_dev = tstd(df[col_x])
	mean_var = mean(df[col_x])

	return {
		"pearson": pearsonr_coefficient,
		"variance": variance, 
		"std_dev": std_dev,
		"mean": mean_var
	}


@app.route("/stats/<predict_type>", methods=["GET", "POST"])
def processStats(predict_type):
	def predictAsma():
		medical_condition = "asma"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	
	def predictCardiovascular():
		medical_condition = "cardiovascular"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictDiabetes():
		medical_condition = "diabetes"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictEmbarazo():
		medical_condition = "embarazo"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictEpoc():
		medical_condition = "epoc"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictHipertension():
		medical_condition = "hipertension"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictInmusupr():
		medical_condition = "inmusupr"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}
		
	def predictNeumonia():
		medical_condition = "neumonia"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictObesidad():
		medical_condition = "obesidad"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictRenal():
		medical_condition = "renal_cronica"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

	def predictTabaquismo():
		medical_condition = "tabaquismo"
		stat_res = getStats(medical_condition.upper(), medical_condition)

		pearson = stat_res["pearson"]
		media = stat_res["mean"]
		varianza = stat_res["variance"]
		desviacion_estandar = stat_res["std_dev"]

		return { 
			"pearson": round(pearson, 4),
			"variance": round(varianza, 4),
			"std_dev": round(desviacion_estandar, 4),
			"mean": round(media, 4)
		}

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

	stats = switch.get(predict_type)
	jsonResult = jsonify(stats)

	return jsonResult

if __name__ == '__main__':
	app.run()