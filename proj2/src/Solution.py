import random
from ProblemData import ProblemData

NUM_DAYS = 5
NUM_TIMESLOTS_PER_DAY = 9
NUM_TIMESLOTS = NUM_DAYS * NUM_TIMESLOTS_PER_DAY


# TODO: Discuss
# After understanding the problem, the best way to represent a solution is an array with the events that are going to take place in each timeslot for each room.
# e.g. if there were 2 days with 2 timeslots each, 4 timeslots total
# if there were 3 rooms, there could be 12 events taking place in total (4 timeslots * 3 rooms)
# first element is timeslot 0 room 0, second is timeslot 0 room 1, third is timeslot 0 room 2, fourth is timeslot 1 room 0, etc

class Solution:
    def __init__(self, solution=[]):
        self.solution = solution
        if (len(self.solution) == 0):
            self.randomize()

    def randomize(self):
        self.solution = [random.randint(0, ProblemData.num_events - 1) for i in range(NUM_TIMESLOTS * ProblemData.num_rooms)]

    def __str__(self):
        return "{}".format(self.solution)

    def isValid(self):
        return self.validStudentConstraint() and self.validRoomSizesConstraint()

    def validStudentConstraint(self):
        return True

    def validRoomSizesConstraint(self):
        for timeslot_num in range(NUM_TIMESLOTS):
            for room_num in range(ProblemData.num_rooms):
                event_num = self.solution[timeslot_num*ProblemData.num_rooms + room_num]
                event = ProblemData.events[event_num]
                room = ProblemData.rooms[room_num]
                if (event.num_attendees > room.size):
                    err = "\nError in timeslot {}:\nEvent {} ({} attendees) can't take place in room {} (size {}).".format(
                        timeslot_num, event_num, event.num_attendees, room_num, room.size)
                    print(err)
                    return False
        return True