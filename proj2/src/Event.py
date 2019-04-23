class Event:
    def __init__(self, id):
        self.id = id
        self.features = set()
        self.attendees = set()

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} (num_attendees={}) : {}".format(self.id, self.getNumAttendees(), self.features)

    def getNumAttendees(self):
        return len(self.attendees)
