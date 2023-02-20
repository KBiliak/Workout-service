from server.model.workout import Workout


class WorkoutRepository:

    def __init__(self, mysql):
        self.mysql = mysql

    def create(self, workout):
        with self.mysql.connection.cursor() as cursor:
            sql = f"INSERT INTO workout (name, description) VALUES " \
                  f"('{workout.name}', '{workout.description}')"
            cursor.execute(sql)
            self.mysql.connection.commit()

    def delete(self, id):
        with self.mysql.connection.cursor() as cursor:
            sql = f"delete from workout where id = {id}"
            cursor.execute(sql)
            self.mysql.connection.commit()


    def get(self):
        with self.mysql.connection.cursor() as cursor:
            sql = f"select * from workout"
            cursor.execute(sql)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                workout = Workout(row[0], row[1], row[2])
                result.append(workout)

        return result

    def get_id(self, id):
        with self.mysql.connection.cursor() as cursor:
            sql = f"select * from workout where id = {id}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            row = rows[0]
            workout = Workout(row[0], row[1], row[2])
        return workout

