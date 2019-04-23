import random
import numpy as np
from ProblemData import ProblemData

# TODO: Discuss
# After understanding the problem, the best way to represent a solution is an array with length equal to the number of events that are going to take place.
# Each element is a number from 0 to (num_timeslots*num_rooms - 1), which means that events in index "i" is taking place in "X", where X is equal to 
# time_slot*num_rooms + room_number
# e.g. There are 2 days with 3 timeslots each (6 timeslots total). There are 5 different rooms. If there were 3 events a solution could be [8, 25, 16]
# event 0 is taking place in timeslot 1, in room number 3 (1*5 + 3 = 8). 
    # given value 8,   timeslot = 8//num_rooms = 8//5 = 1    and    room_number = 8%num_rooms = 8%5 = 3
# event 1 is taking place in timeslot 5, in room number 0 (5*5 + 0 = 25)
# event 2 is taking place in timeslot 3, in room number 1 (3*5 + 1 = 16)

class Solution:
    def __init__(self, solution=[]):
        self.solution = solution
        if (len(self.solution) == 0):
            self.randomize()

    def randomize(self):
        sol = set()
        while(len(sol) < ProblemData.num_events):
            sol.add(random.randint(0, ProblemData.NUM_TIMESLOTS*ProblemData.num_rooms - 1))
        self.solution = list(sol)

    def __str__(self):
        return "{}".format(self.solution)

    # Verify if the solution respects all the Hard Constraints
    def isValid(self):
        return self.validStudentConstraint() and self.validRoomSizesConstraint() and self.repeatedEventConstraint()

    # Hard Constraint
    # Verify if only one event is in each room at any timeslot.
    def repeatedEventConstraint(self):
        return np.unique(self.solution).size == len(self.solution)
        
    # Hard Constraint
    # Verify if a student isn't "trying" to attend two different events in the same timeslot
    def validStudentConstraint(self):
        for student in ProblemData.students:
            student_occupied_timeslots = [False] * ProblemData.NUM_TIMESLOTS
            for event_num in range(len(self.solution)):
                if student.attends(event_num):
                    event_timeslot = self.solution[event_num]//ProblemData.num_rooms
                    if student_occupied_timeslots[event_timeslot]:
                        print("\nError: Student {} can't participate in more than one event in timeslot {}.".format(
                            student.id, event_timeslot))
                        return False
                    student_occupied_timeslots[event_timeslot] = True
        return True

    # Hard Constraint
    # Verify if the rooms which the events were allocated to are big enough to hold the number of attendees of the event
    def validRoomSizesConstraint(self):
        for i in range(len(self.solution)):
            room = ProblemData.rooms[self.solution[i] % ProblemData.num_rooms]
            event = ProblemData.events[i]
            if (event.num_attendees > room.size):
                print("\nError in timeslot {}:\nEvent {} ({} attendees) can't take place in room {} (size {}).".format(
                    timeslot_num, event_num, event.num_attendees, room_num, room.size))
                return False
            if not event.canTakePlaceInRoom(room):
                print("\nError in timeslot {}:\nEvent {} can't take place in room {} due to incompatibility.".format(
                    timeslot_num, event_num, event.num_attendees))
                return False
        return True

    # Verify solution Soft Constraints and compute the amount of penalty for the ones that are not respected
    def penalty(self):
        return  self.penaltySingleEventAndConcutiveEvents() + self.penaltyEndOfDayEvent()

    # Soft Constraint
    # TODO
    def penaltySingleEventAndConcutiveEvents(self):
        # return 0
        # only_1_class_count = 0
        # consecutive_penalty = 0
        # for student in ProblemData.students:
        #     for day_num in range(ProblemData.NUM_DAYS):
        #         num_events_this_day = 0
        #         consecutive_timeslot_with_event = 0
        #         for timeslot_num in range(ProblemData.NUM_TIMESLOTS_PER_DAY):
        #             is_participating = False
        #             for room_num in range(ProblemData.num_rooms):
        #                 event_num = self.solution[
        #                     day_num*ProblemData.NUM_TIMESLOTS_PER_DAY*ProblemData.num_rooms + timeslot_num*ProblemData.num_rooms + room_num
        #                 ]
        #                 if (event_num is not None):
        #                     num_events_this_day += student.attends(event_num)
        #                     consecutive_timeslot_with_event += 1
        #                     is_participating = True
        #                     if (consecutive_timeslot_with_event >= 3):
        #                         consecutive_penalty += 1
        #             if not is_participating:
        #                 consecutive_timeslot_with_event = 0
        #         only_1_class_count += 1 if (num_events_this_day == 1) else 0
        # print("DBG::penalty1()::only_1_class_count:: " + str(only_1_class_count))
        # print("DBG::penalty1()::consecutive_penalty:: " + str(consecutive_penalty))
        # return only_1_class_count + consecutive_penalty
        return 0

    # Soft Constraint
    # Count the number of occurrences of a student attending an event in the last timeslot of the day (number of attendees of each 
    # event that takes place in the last timeslot of each day)
    def penaltyEndOfDayEvent(self):
        penalty = 0
        for event_num in range(len(self.solution)):
            if (self.solution[event_num] % ProblemData.num_events_per_day in range(ProblemData.num_events_per_day - ProblemData.num_rooms, ProblemData.num_events_per_day)):
                penalty += ProblemData.events[event_num].num_attendees
        return penalty