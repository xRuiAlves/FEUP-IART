class Room:
    def __init__(self, id, num_features, size):
        self.id = id
        self.size = size
        self.features = [0] * num_features

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return "{} (size={}) : {}".format(self.id, self.size, self.features)

    def addFeature(self, feature_id):
        self.features[feature_id] = 1
    
    def hasFeature(self, feature_id):
        return self.features[feature_id]
