import sys

from Student import Student
from Event import Event
from Room import Room

class FileReader:
    def __init__(self):
        self.students = []
        self.events = []
        self.rooms = []

    def readFile(self, file_name):
        try:
            file = open(file_name , "r")
        except IOError:
            sys.stderr.write("Input file not found.\n")
            sys.exit(2)

        [num_events, num_rooms, num_features, num_students] = list(map(int, file.readline().rstrip().split(" ")))
        
        # Parse rooms
        for i in range(num_rooms):
            room_size = int(file.readline())
            self.rooms.append(Room(i, room_size))

        self.events = [Event(i) for i in range(num_events)]

        # Parse students
        for i in range(num_students):
            self.students.append(Student(i))
            for j in range(num_events):
                is_participating = int(file.readline())
                if is_participating:
                    self.students[i].events.add(j)
                    self.events[j].num_attendees += 1
        
        # Parse rooms
        for i in range(num_rooms):
            for j in range(num_features):
                contains_feature = int(file.readline())
                if contains_feature:
                    self.rooms[i].features.add(j)
        
        # Parse events
        for i in range(num_events):
            for j in range(num_features):
                needs_feature = int(file.readline())
                if needs_feature:
                    self.events[i].features.add(j)
            
        print("Input parsing completed.\nNumber of students: {}\nNumber of events: {}\nNumber of rooms: {}".format(
            len(self.students), 
            len(self.events),
            len(self.rooms)
        ))