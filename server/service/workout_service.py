
class WorkoutService:

    def __init__(self, repository):
        self.repository = repository

    def create(self, workout):
        self.repository.create(workout)


    def delete(self, id):
        self.repository.delete(id)

    def get(self):
        return self.repository.get()

    def get_id(self, id):
        return self.repository.get_id(id)
