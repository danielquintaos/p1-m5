from flask import Flask
from flask import request, jsonify
from flask import render_template
from flask import redirect, url_for
from tinydb import TinyDB, Query


app = Flask(__name__)
db = TinyDB('caminhos.json')
games_table = db.table('game')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<action>', methods = ['POST'])
def action(action):
	response = {
	'action' : action
	}

	return render_template('index.html', **response)