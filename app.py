# This file contains the code for the Flask application

from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from models import ActivityType

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Arnold!24@localhost/RunningApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/activitytypes', methods=['GET'])
def get_activity_types():
    activity_types = ActivityType.query.all()
    return jsonify({'activity_type': [activity_type.to_dict() for activity_type in activity_types]})

if __name__ == '__main__':
    app.run()
