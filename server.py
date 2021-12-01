import sys
from flask import Flask, render_template, request, redirect, Response
import random, json


app = Flask(__name__)


@app.route('/')
def output():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)