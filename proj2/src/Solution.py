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

    # Verify if the solution respects all the Hard Constraints
    def isValid(self):
        return self.validStudentConstraint() and self.validRoomSizesConstraint()

    # Hard Constraint
    # Verify if a student isn't "trying" to attend two different events in the same timeslot
    def validStudentConstraint(self):
        for student in ProblemData.students:
            for timeslot_num in range(NUM_TIMESLOTS):
                is_attending = False
                for room_num in range(ProblemData.num_rooms): 
                    event_num = self.solution[timeslot_num*ProblemData.num_rooms + room_num]
                    if (student.attends(event_num)):
                        if is_attending:    # Attending two events in same timeslot!!
                            err = "\nError in timeslot {}:\nStudent {} is attending more than 1 event.".format(
                                timeslot_num, student.id)
                            print(err)
                            return False 
                        else:
                            is_attending = True

    # Hard Constraint
    # Verify if the rooms which the events were allocated to are big enough to hold the number of attendees of the event
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

    # Verify solution Soft Constraints and compute the amount of penalty for the ones that are not respected
    def penalty(self):
        return  self.penalty1() + self.penalty2() + self.penaltyEndOfDayClass()

    # Soft Constraint
    # TODO
    def penalty1(self):
        return 0

    # Soft Constraint
    # TODO
    def penalty2(self):
        return 0

    # Soft Constraint
    # Count the number of occurrences of a student attending an event in the last timeslot of the day (number of attendees of each 
    # event that takes place in the last timeslot of each day)
    def penaltyEndOfDayClass(self):
        penalty = 0
        for day_num in range(NUM_DAYS):
            for room_num in range(ProblemData.num_rooms):
                event_num = self.solution[day_num*NUM_TIMESLOTS_PER_DAY*ProblemData.num_rooms + (NUM_TIMESLOTS_PER_DAY-1)*ProblemData.num_rooms + room_num]
                penalty += ProblemData.events[event_num].num_attendees
        return penalty