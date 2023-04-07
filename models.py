from database import db

class ActivityType(db.Model):
    __tablename__ = 'activitytypeinfo'
    __table_args__ = {'extend_existing': True}
    activity_type_id = db.Column(db.Integer, primary_key=True)
    activity_type_name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {
            'activity_type_id': self.activity_type_id,
            'activity_type_name': self.activity_type_name
        }

class Courses(db.Model):
    # Define attributes for this table
    __tablename__ = 'courses'
    __table_args__ = {'extend_existing': True}
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255), unique=True, nullable=False)
    course_location = db.Column(db.String(255), nullable=False)
    course_distance = db.Column(db.Integer, nullable=False)
    course_terrain = db.Column(db.String(255), nullable=True)
    course_difficulty = db.Column(db.String(255), nullable=True)

class Difficulty(db.Model):
    __tablename__ = 'difficultyinfo'
    __table_args__ = {'extend_existing': True}
    difficulty_id = db.Column(db.Integer, primary_key=True)
    difficulty_name = db.Column(db.String(255), unique=True, nullable=False)

class Shoes(db.Model):
    __tablename__ = 'shoesinfo'
    __table_args__ = {'extend_existing': True}
    shoes_id = db.Column(db.Integer, primary_key=True)
    shoes_name = db.Column(db.String(255), unique=True, nullable=False)
    shoes_brand = db.Column(db.String(255), unique=True, nullable=True)

class Terrain(db.Model):
    __tablename__ = 'terraininfo'
    __table_args__ = {'extend_existing': True}
    terrain_id = db.Column(db.Integer, primary_key=True)
    terrain_name = db.Column(db.String(255), unique=True, nullable=False)

class WeatherCondition(db.Model):
    __tablename__ = 'weatherconditioninfo'
    __table_args__ = {'extend_existing': True}
    weathercondition_id = db.Column(db.Integer, primary_key=True)
    weathercondition_name = db.Column(db.String(255), unique=True, nullable=False)

class WeatherWind(db.Model):
    __tablename__ = 'weatherwindinfo'
    __table_args__ = {'extend_existing': True}
    weatherwind_id = db.Column(db.Integer, primary_key=True)
    weatherwind_name = db.Column(db.String(255), unique=True, nullable=False)

class WorkoutType(db.Model):
    __tablename__ = 'workouttypeinfo'
    __table_args__ = {'extend_existing': True}
    workouttype_id = db.Column(db.Integer, primary_key=True)
    workouttype_name = db.Column(db.String(255), unique=True, nullable=False)

# Define additional models as needed
