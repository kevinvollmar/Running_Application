# This file contains the code for the Flask application

from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from models import ActivityType, Courses, Shoes, Terrain, WorkoutType

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

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Courses.query.all()
    return jsonify({'course': [course.to_dict() for course in courses]})

@app.route('/api/shoesinfo', methods=['GET'])
def get_shoesinfo():
    shoes = Shoes.query.all()
    return jsonify({'shoesinfo': [shoe.to_dict() for shoe in shoes]})

@app.route('/api/terraininfo', methods=['GET'])
def get_terraininfo():
    terrains = Terrain.query.all()
    return jsonify({'terraininfo': [terrain.to_dict() for terrain in terrains]})

@app.route('/api/workouttypeinfo', methods=['GET'])
def get_workout_types():
    workout_types = WorkoutType.query.all()
    return jsonify({'workout_type': [workout_type.to_dict() for workout_type in workout_types]})

if __name__ == '__main__':
    app.run()
