class Event:
    def __init__(self, id, num_attendees=0):
        self.id = id
        self.features = set()
        self.num_attendees = num_attendees

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} (num_attendees={}) : {}".format(self.id, self.num_attendees, self.features)
