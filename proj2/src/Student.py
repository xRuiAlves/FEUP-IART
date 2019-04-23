class Student:
    def __init__(self, id, num_events):
        self.id = id
        self.events = [0] * num_events

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} : {}".format(self.id, self.events)

    def addEvent(self, event_id):
        self.events[event_id] = 1
    
    def needsFeature(self, event_id):
        return self.events[event_id]
