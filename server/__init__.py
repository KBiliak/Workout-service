from flask import Flask
from flask_mysqldb import MySQL
from server.repository.workout_repository import WorkoutRepository
from server.service.workout_service import WorkoutService

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'workout_db'

mysql = MySQL(app)

workoutRepository = WorkoutRepository(mysql)
workoutService = WorkoutService(workoutRepository)

import server.endpoint.workout_endpoint