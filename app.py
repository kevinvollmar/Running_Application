# This file contains the code for the Flask application

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'name': 'John', 'age': 30}
    response = jsonify(data)
    return response
