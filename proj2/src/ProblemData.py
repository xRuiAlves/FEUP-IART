import sys

from Student import Student
from Event import Event
from Room import Room

class ProblemData:
    NUM_DAYS = 2
    NUM_TIMESLOTS_PER_DAY = 3
    NUM_TIMESLOTS = NUM_DAYS * NUM_TIMESLOTS_PER_DAY
    students = []
    events = []
    rooms = []
    num_events = None
    num_rooms = None
    num_features = None
    num_students = None

    @staticmethod
    def readFile( file_name):
        try:
            file = open(file_name , "r")
        except IOError:
            sys.stderr.write("Error: Input file not found.\n")
            sys.exit(2)

        [ProblemData.num_events, ProblemData.num_rooms, ProblemData.num_features, ProblemData.num_students] = list(map(int, file.readline().rstrip().split(" ")))
        
        if (ProblemData.num_events > ProblemData.NUM_TIMESLOTS):
            sys.stderr.write("Error: Number of events ({}) is higher than the number of rooms multiplied by number of available timeslots ({}).".format(
                ProblemData.num_events,
                ProblemData.NUM_TIMESLOTS * ProblemData.num_rooms
            ))
            sys.exit(3)

        # Create rooms
        for i in range(ProblemData.num_rooms):
            room_size = int(file.readline())
            ProblemData.rooms.append(Room(i, ProblemData.num_features, room_size))

        ProblemData.events = [Event(i, ProblemData.num_features, ProblemData.num_students) for i in range(ProblemData.num_events)]

        # Parse students
        for i in range(ProblemData.num_students):
            ProblemData.students.append(Student(i, ProblemData.num_events))
            for j in range(ProblemData.num_events):
                is_participating = int(file.readline())
                if is_participating:
                    ProblemData.students[i].addEvent(j)
                    ProblemData.events[j].addAttendee(i)
        
        # Parse rooms
        for i in range(ProblemData.num_rooms):
            for j in range(ProblemData.num_features):
                contains_feature = int(file.readline())
                if contains_feature:
                    ProblemData.rooms[i].addFeature(j)
        
        # Parse events
        for i in range(ProblemData.num_events):
            for j in range(ProblemData.num_features):
                needs_feature = int(file.readline())
                if needs_feature:
                    ProblemData.events[i].addFeature(j)
            
        print("Input parsing completed.\nNumber of students: {}\nNumber of events: {}\nNumber of rooms: {}".format(
            len(ProblemData.students), 
            len(ProblemData.events),
            len(ProblemData.rooms)
        ))