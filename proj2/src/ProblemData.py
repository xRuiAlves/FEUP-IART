import sys

from Student import Student
from Event import Event
from Room import Room

class ProblemData:
    students = []
    events = []
    rooms = []

    @staticmethod
    def readFile( file_name):
        try:
            file = open(file_name , "r")
        except IOError:
            sys.stderr.write("Input file not found.\n")
            sys.exit(2)

        [num_events, num_rooms, num_features, num_students] = list(map(int, file.readline().rstrip().split(" ")))
        
        # Parse rooms
        for i in range(num_rooms):
            room_size = int(file.readline())
            ProblemData.rooms.append(Room(i, room_size))

        ProblemData.events = [Event(i) for i in range(num_events)]

        # Parse students
        for i in range(num_students):
            ProblemData.students.append(Student(i))
            for j in range(num_events):
                is_participating = int(file.readline())
                if is_participating:
                    ProblemData.students[i].events.add(j)
                    ProblemData.events[j].num_attendees += 1
        
        # Parse rooms
        for i in range(num_rooms):
            for j in range(num_features):
                contains_feature = int(file.readline())
                if contains_feature:
                    ProblemData.rooms[i].features.add(j)
        
        # Parse events
        for i in range(num_events):
            for j in range(num_features):
                needs_feature = int(file.readline())
                if needs_feature:
                    ProblemData.events[i].features.add(j)
            
        print("Input parsing completed.\nNumber of students: {}\nNumber of events: {}\nNumber of rooms: {}".format(
            len(ProblemData.students), 
            len(ProblemData.events),
            len(ProblemData.rooms)
        ))

    @staticmethod
    def getNumStudents():
        return len(ProblemData.students)

    @staticmethod
    def getNumEvents():
        return len(ProblemData.events)

    @staticmethod
    def getNumRooms():
        return len(ProblemData.rooms)