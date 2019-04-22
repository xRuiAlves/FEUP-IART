class Event:
    def __init__(self, id):
        self.id = id
        self.features = set()

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} : {}".format(self.id, self.features)
