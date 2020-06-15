from flask import Flask, render_template, url_for, request

import pandas as pd
import numpy as np
import scipy

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
	# obesity_file = os.path.realpath("../output.csv")
	# model = linear_model.LinearRegression()
	# OBESITY_covid_data = pd.read_csv(obesity_file, encoding='cp1252')

	# data = OBESITY_covid_data[["OBESIDAD", "DEATHS_PER_DAY"]]
	# X = OBESITY_covid_data[["OBESIDAD"]]
	# y = OBESITY_covid_data[["DEATHS_PER_DAY"]]

	# model.fit(X, y)

	# predicted = model.predict([[20]])
	# print("Prediction: ", predicted)

	# obesidad = OBESITY_covid_data["OBESIDAD"]
	# muertes = OBESITY_covid_data["DEATHS_PER_DAY"]

	# pearsonr_coefficient, p_value = pearsonr(obesidad, muertes)
	# determination_score  = r2_score(obesidad, muertes)

	# print("Pearson Coefficient: ", pearsonr_coefficient)
	# print("R2 determination: {}".format(determination_score, ".3f"))
	# print(data.cov() + "\n\n\n")
	#sb.scatterplot(obesidad, muertes)
	#sb.regplot(obesidad, muertes, marker="+")
	return render_template("index.html")

@app.route("/getCorrelation", methods=["GET", "POST"])
def getCorrelation():
	print(request.method)
	if request.method == "POST":
		selected_illness = request.form["illness-select"]
		print(selected_illness)

		illness_file = os.path.realpath(f"./ProyectoProba/Enfermedades/{selected_illness}.csv")
    	covid_data = pd.read_csv(illness_file, encoding='cp1252')

		column = covid_data[selected_illness.upper()]
    	deaths = covid_data["DEATHS_PER_DAY"]

		pearsonr_coefficient, p_value = pearsonr(column, deaths)
    	determination_score  = r2_score(column, deaths)

		

		return str(selected_illness)

if __name__ == '__main__':
	app.run()