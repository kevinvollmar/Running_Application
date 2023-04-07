from flask import Flask, jsonify
from database import db
from models import ActivityType
from app import app

app = Flask(__name__)

@app.route('/api/activitytypes', methods=['GET'])
def get_activity_types():
    activity_types = ActivityType.query.all()
    return jsonify({'activity_type': [activity_type.to_dict() for activity_type in activity_types]})
