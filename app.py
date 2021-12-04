from flask import Flask, render_template, request
import json
from modules.bisection import bisection
from modules.falseposition import false_position
from modules.newtonrhapson import newton_rhapson
from modules.secant import secant
from modules.sifi import sifi
from modules.nonlinear import nonlinear
import pandas as pd
import traceback

app = Flask(__name__)


@app.route('/receiver', methods = ['POST'])
def compute():
	try:
		print("===== REQUEST RECEIVED =====")
		data = json.loads(request.get_data())
		method = data['selected']
		toReturn = {"table":"","final":""}
		print(data)

		crit = float(data['crit'])
		if method == "Non-linear":
			eq1l = data['eq1l']
			eq1r = data['eq1r']
			eq2l = data['eq2l']
			eq2r = data['eq2r']
			x0 = float(data['x0'])
			y0 = float(data['y0'])
		elif method == "Newton Rhapson" or method == "Simple Fix Iteration":
			eq = data['eq']
			x = float(data['x'])
		else:
			eq = data['eq']
			xl = float(data['xl'])
			xu = float(data['xu'])

		# TODO: Newton Rhapson infinite loop(?) - show error prompt
		start_str = "Root: = "
		if method == "Bisection":
			d = bisection(eq, xl, xu, crit)
			toReturn['final'] = start_str + str(d.iloc[-1].at["xr"])
			toReturn['table'] = d.to_html()
		if method == "False Position":
			d = false_position(eq, xl, xu, crit)
			toReturn['final'] = start_str + str(d.iloc[-1].at["xr"])
			toReturn['table'] = d.to_html()
		if method == "Newton Rhapson":
			d = newton_rhapson(eq, x, crit)
			toReturn['final'] = start_str + str(d.iloc[-1].at["f_x"])
			toReturn['table'] = d.to_html()
		if method == "Secant":
			d = secant(eq, xl, xu, crit)
			toReturn['final'] = start_str + str(d.iloc[-1].at["x_b"])
			toReturn['table'] = d.to_html()
		if method == "Simple Fix Iteration":
			d = sifi(eq, x, crit)
			toReturn['final'] = start_str + str(d.iloc[-1].at["f_x"])
			toReturn['table'] = d.to_html()
		if method == "Non-linear":
			print("Nonlinear")
			d = nonlinear(eq1l, eq1r, eq2l, eq2r, x0, y0, crit)
			var1 = d.iloc[-1].iat[1]
			var2 = d.iloc[-1].iat[2]
			toReturn['final'] = "Solution: <br>" + eq1l + " = " + str(var1) + ", " + eq2l + " = " + str(var2)
			toReturn['table'] = d.to_html()
	
		return json.dumps(toReturn)
	except Exception as e:
		traceback.print_exc()
		# print(e)
		return "<p><b>Invalid Input</b></p>"

@app.route('/')
def output():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)