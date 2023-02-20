class Workout:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Workout(id={self.id}, name={self.name}, " \
               f"description={self.description})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
