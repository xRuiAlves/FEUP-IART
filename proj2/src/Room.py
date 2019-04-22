class Room:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.features = set()

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} (size={}) : {}".format(self.id, self.size, self.features)
