class Event:
    def __init__(self, id, num_features, num_students):
        self.id = id
        self.features = [0] * num_features
        self.attendees = [0] * num_students
        self.num_attendees = 0

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} : {}".format(self.id, self.features)

    def addFeature(self, feature_id):
        self.features[feature_id] = 1
    
    def needsFeature(self, feature_id):
        return self.features[feature_id]

    def addAttendee(self, attendee_id):
        self.attendees[attendee_id] = 1
        self.num_attendees += 1
    
    def hasAttendee(self, attendee_id):
        return self.attendees[attendee_id]

    def canTakePlaceInRoom(self, room):
        for feature_num in range(len(self.features)):
            if self.features[feature_num]:
                if not room.hasFeature(feature_num):
                    return False
        return True
