import random
import numpy as np
from ProblemData import ProblemData

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
        self.solution = [i for i in range(ProblemData.num_events)] + [None]*(ProblemData.NUM_TIMESLOTS*ProblemData.num_rooms - ProblemData.num_events)
        random.shuffle(self.solution)

    def __str__(self):
        return "{}".format(self.solution)

    # Verify if the solution respects all the Hard Constraints
    def isValid(self):
        return self.validStudentConstraint() and self.validRoomSizesConstraint() and self.repeatedEventConstraint()

    # Hard Constraint
    # Verify if an event only occurs once in all timeslots (when mutations and crossovers occur this contraint may not be kept, needs verification!)
    def repeatedEventConstraint(self):
        events = [event for event in self.solution if event is not None]
        return np.unique(events).size == len(events)
        

    # Hard Constraint
    # Verify if a student isn't "trying" to attend two different events in the same timeslot
    def validStudentConstraint(self):
        for student in ProblemData.students:
            for timeslot_num in range(ProblemData.NUM_TIMESLOTS):
                is_attending = False
                for room_num in range(ProblemData.num_rooms): 
                    event_num = self.solution[timeslot_num*ProblemData.num_rooms + room_num]
                    if (event_num is not None and student.attends(event_num)):
                        if is_attending:    # Attending two events in same timeslot!!
                            err = "\nError in timeslot {}:\nStudent {} is attending more than 1 event.".format(
                                timeslot_num, student.id)
                            print(err)
                            return False 
                        else:
                            is_attending = True
        return True

    # Hard Constraint
    # Verify if the rooms which the events were allocated to are big enough to hold the number of attendees of the event
    def validRoomSizesConstraint(self):
        for timeslot_num in range(ProblemData.NUM_TIMESLOTS):
            for room_num in range(ProblemData.num_rooms):
                event_num = self.solution[timeslot_num*ProblemData.num_rooms + room_num]
                if (event_num is None):
                    continue
                event = ProblemData.events[event_num]
                room = ProblemData.rooms[room_num]
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
        return  self.penalty1() + self.penalty2() + self.penaltyEndOfDayEvent()

    # Soft Constraint
    # TODO
    def penaltySingleEvent(self):
        only_1_class_count = 0
        consecutive_penalty = 0
        for student in ProblemData.students:
            for day_num in range(ProblemData.NUM_DAYS):
                num_events_this_day = 0
                consecutive_timeslot_with_event = 0
                for timeslot_num in range(ProblemData.NUM_TIMESLOTS_PER_DAY):
                    is_participating = False
                    for room_num in range(ProblemData.num_rooms):
                        event_num = self.solution[
                            day_num*ProblemData.NUM_TIMESLOTS_PER_DAY*ProblemData.num_rooms + timeslot_num*ProblemData.num_rooms + room_num
                        ]
                        if (event_num is not None):
                            num_events_this_day += student.attends(event_num)
                            consecutive_timeslot_with_event += 1
                            is_participating = True
                            if (consecutive_timeslot_with_event >= 3):
                                consecutive_penalty += 1
                    if not is_participating:
                        consecutive_timeslot_with_event = 0
                only_1_class_count += 1 if (num_events_this_day == 1) else 0
        print("DBG::penalty1()::only_1_class_count:: " + str(only_1_class_count))
        print("DBG::penalty1()::consecutive_penalty:: " + str(consecutive_penalty))
        return only_1_class_count + consecutive_penalty

    # Soft Constraint
    # TODO
    def penalty2(self):
        return 0

    # Soft Constraint
    # Count the number of occurrences of a student attending an event in the last timeslot of the day (number of attendees of each 
    # event that takes place in the last timeslot of each day)
    def penaltyEndOfDayEvent(self):
        penalty = 0
        for day_num in range(ProblemData.NUM_DAYS):
            for room_num in range(ProblemData.num_rooms):
                event_num = self.solution[day_num*ProblemData.NUM_TIMESLOTS_PER_DAY*ProblemData.num_rooms + (ProblemData.NUM_TIMESLOTS_PER_DAY-1)*ProblemData.num_rooms + room_num]
                if (event_num is None):
                    continue
                penalty += ProblemData.events[event_num].num_attendees
        print("DBG::penaltyEndOfDayEvent():: " + str(penalty))
        return penalty