'''Here is some starter code for a Flask Web Application. Expand on that and include
 a route that simulates rolling two dice and returns the result in JSON. You should 
 include a brief explanation of your code.'''

from flask import Flask, jsonify

app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/JSON')
def rollDice():
	numOfDie = 2
	die = 0
	list = {}
	def genNumber():
		a = random.randrange(1,6)
		return a
	for die in range(die,numOfDie):
		dieRoll = genNumber()
		list[str(die)] = dieRoll

	return jsonify(list)

if __name__ == '__main__':
	app.debug = True
	app.run()