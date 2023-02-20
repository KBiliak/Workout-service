from flask import request
from server import workoutService, app
from server.model.workout import Workout


@app.get('/workout')
def get_workouts():
    workouts = workoutService.get()
    result = []
    for workout in workouts:
        result.append(workout.to_dict())
    return result


@app.get('/workout/<int:id>')
def get_workout_by_id(id):
    print("get workout by id", id)
    workout = workoutService.get_id(id)
    return workout.to_dict()


@app.delete('/workout/<int:id>')
def delete_workout_by_id(id):
    print(f"Workout by id {id} was deleted")
    workoutService.delete(id)
    return {"200": "workout was deleted"}



@app.post('/workout')
def create_workout():
    body = request.get_json()
    print(f"Create workout: request body = {body}")
    workout = Workout(None, body['name'], body['description'])
    workoutService.create(workout)
    return {}, 201



