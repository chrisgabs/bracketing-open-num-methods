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
		print("===== REQUEST RECEIVED =====")
		data = json.loads(request.get_data())
		method = data['selected']
		toReturn = {"table":"","final":""}
		print(data)

		eq = data['eq']
		crit = float(data['crit'])
		if method == "Non-linear":
			return
		elif method == "Newton Rhapson" or method == "Simple Fix Iteration":
			x = float(data['x'])
		else:
			xl = float(data['xl'])
			xu = float(data['xu'])

		# TODO: parse final answer for secant and non-linear (ask arian)
		if method == "Bisection":
			d = bisection(eq, xl, xu, crit)
			toReturn['final'] = d.iloc[-1].at["xr"]
			toReturn['table'] = d.to_html()
		if method == "False Position":
			d = false_position(eq, xl, xu, crit)
			toReturn['final'] = d.iloc[-1].at["xr"]
			toReturn['table'] = d.to_html()
		if method == "Newton Rhapson":
			d = newton_rhapson(eq, x, crit)
			toReturn['final'] = d.iloc[-1].at["f_x"]
			toReturn['table'] = d.to_html()
		if method == "Secant":
			d = secant(eq, xl, xu, crit)
		if method == "Simple Fix Iteration":
			d = sifi(eq, x, crit)
			toReturn['final'] = d.iloc[-1].at["f_x"]
			toReturn['table'] = d.to_html()
		
		return json.dumps(toReturn)
	except Exception as e:
		print(e)
		return "<p>Invalid Input</p>"

@app.route('/')
def output():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)