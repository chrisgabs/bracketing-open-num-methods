from flask import Flask, render_template, request
import json
from modules.bisection import bisection
from modules.falseposition import false_position
from modules.newtonrhapson import newton_rhapson
from modules.secant import secant
from modules.sifi import sifi
import pandas as pd

app = Flask(__name__)


@app.route('/receiver', methods = ['POST'])
def compute():
	try:
		data = json.loads(request.get_data())
		print(data)
		method = data['selected']

		eq = data['eq']
		crit = float(data['crit'])
		if method == "Non-linear":
			return
		elif method == "Newton Rhapson" or method == "Simple Fix Iteration":
			x = float(data['x'])
		else:
			xl = float(data['xl'])
			xu = float(data['xu'])

		if method == "Bisection":
			return bisection(eq, xl, xu, crit)
		if method == "False Position":
			return false_position(eq, xl, xu, crit)
		if method == "Newton Rhapson":
			return newton_rhapson(eq, x, crit)
		if method == "Secant":
			return secant(eq, xl, xu, crit)
		if method == "Simple Fix Iteration":
			return sifi(eq, x, crit)
	except Exception as e:
		print(e)
		return "<p>Invalid Input</p>"

@app.route('/')
def output():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)