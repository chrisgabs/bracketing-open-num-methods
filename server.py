from flask import Flask, render_template, request
import json
from modules.bisection import bisection


app = Flask(__name__)


@app.route('/receiver', methods = ['POST'])
def compute():
	data = json.loads(request.get_data())
	eq = data['eq']
	xl = float(data['xl'])
	xu = float(data['xu'])
	crit = float(data['crit'])
	return bisection(eq, xl, xu, crit)


@app.route('/')
def output():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)