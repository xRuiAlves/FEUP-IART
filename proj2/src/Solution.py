import random
import math
from ProblemData import ProblemData

# TODO: Discuss
# After understanding the problem, the best way to represent a solution is an array with length equal to the number of events that are going to take place.
# Each element is a number from 0 to (num_timeslots*num_rooms - 1), which means that events in index "i" is taking place in "X", where X is equal to 
# time_slot*num_rooms + room_number
# e.g. There are 2 days with 3 timeslots each (6 timeslots total). There are 5 different rooms. If there were 3 events a solution could be [8, 25, 16]
# event 0 is taking place in timeslot 1, in room number 3 (1*5 + 3 = 8). 
    # given value 8,   
    # timeslot = 8//num_rooms = 8//5 = 1
    # room_number = 8%num_rooms = 8%5 = 3
    # day = timeslot//num_timeslots_per_day = 1//3 = 0
# event 1 is taking place in timeslot 5, in room number 0 (5*5 + 0 = 25)
# event 2 is taking place in timeslot 3, in room number 1 (3*5 + 1 = 16)

class Solution:
    def __init__(self, solution=[]):
        self.solution = solution
        if (len(self.solution) == 0):
            self.randomize()    
        self.is_valid = self.calculateValidity()
        self.penalty = self.calcPenalty()
        self.fitness = 1/(self.penalty+1) if self.is_valid else 0

    def randomize(self):
        sol = set()
        while(len(sol) < ProblemData.num_events):
            sol.add(random.randint(0, ProblemData.NUM_TIMESLOTS*ProblemData.num_rooms - 1))
        self.solution = list(sol)
        random.shuffle(self.solution)

    def isOptimal(self):
        return self.fitness == 1

    def mutate(self):
        for i in range(len(self.solution)):
            self.solution[i] = random.randint(0, ProblemData.NUM_TIMESLOTS*ProblemData.num_rooms - 1)
        self.is_valid = self.calculateValidity()
        self.penalty = self.calcPenalty()
        self.fitness = 1/(self.penalty+1) if self.is_valid else 0

    @staticmethod
    def crossover(s1, s2):
        mid_point = random.randint(0, ProblemData.num_events)
        child1 = s1.solution[0:mid_point] + s2.solution[mid_point:ProblemData.num_events]
        child2 = s2.solution[0:mid_point] + s1.solution[mid_point:ProblemData.num_events]
        return [Solution(child1), Solution(child2)]

    def __str__(self):
        if (self.fitness != 0):
            return "{}\tpenalty={}, fitness={}".format(self.solution, self.penalty, self.fitness)
        else:
            return "{}\tInvalid Solution".format(self.solution)

    # Verify if the solution respects all the Hard Constraints
    def calculateValidity(self):
        return self.validStudentConstraint() and self.validRoomSizesConstraint() and self.repeatedEventConstraint()

    # Hard Constraint
    # Verify if only one event is in each room at any timeslot.
    def repeatedEventConstraint(self):
        return len(set(self.solution)) == len(self.solution)
        
    # Hard Constraint
    # Verify if a student isn't "trying" to attend two different events in the same timeslot
    def validStudentConstraint(self, debug=False):
        for student in ProblemData.students:
            student_occupied_timeslots = [False] * ProblemData.NUM_TIMESLOTS
            for event_num in range(len(self.solution)):
                if student.attends(event_num):
                    event_timeslot = self.solution[event_num]//ProblemData.num_rooms
                    if student_occupied_timeslots[event_timeslot]:
                        if debug:
                            print("\nError: Student {} can't participate in more than one event in timeslot {}.".format(
                                student.id, event_timeslot))
                        return False
                    student_occupied_timeslots[event_timeslot] = True
        return True

    # Hard Constraint
    # Verify if the rooms which the events were allocated to are big enough to hold the number of attendees of the event
    def validRoomSizesConstraint(self, debug=False):
        for i in range(len(self.solution)):
            room = ProblemData.rooms[self.solution[i] % ProblemData.num_rooms]
            event = ProblemData.events[i]
            if (event.num_attendees > room.size):
                if debug:
                    print("\nError:\nEvent {} ({} attendees) can't take place in room {} (size {}).".format(
                        event.id, event.num_attendees, room.id, room.size))
                return False
            if not event.canTakePlaceInRoom(room):
                if debug:
                    print("\nError:\nEvent {} can't take place in room {} due to incompatibility.".format(
                        event.id, event.num_attendees))
                return False
        return True

    # Verify solution Soft Constraints and compute the amount of penalty for the ones that are not respected
    def calcPenalty(self):
        return  self.penaltySingleEventAndConcutiveEvents() + self.penaltyEndOfDayEvent()

    # Soft Constraint
    # Computes 2 soft constraints: 
    # 1) Count the number of times each student has a single class in each of the days
    # 2) Count the number of consecutive class blocks within each day and compute its penalty
    def penaltySingleEventAndConcutiveEvents(self, debug=False):
        only_1_class_count = 0
        consecutive_penalty = 0
        for student in ProblemData.students:
            events_per_day = [0] * ProblemData.NUM_DAYS # array containing [TimeslotNumber, ConsecutiveCount]
            events_per_timeslot_per_day = [ [ 0 for i in range(ProblemData.NUM_TIMESLOTS_PER_DAY) ] for j in range(ProblemData.NUM_DAYS) ]
            for event_num in range(len(self.solution)):
                if (student.attends(event_num)):
                    timeslot = self.solution[event_num]//ProblemData.num_rooms
                    timeslot_in_day = timeslot%ProblemData.NUM_TIMESLOTS_PER_DAY
                    event_day = timeslot//ProblemData.NUM_TIMESLOTS_PER_DAY
                    events_per_day[event_day] += 1 
                    events_per_timeslot_per_day[event_day][timeslot_in_day] += 1
            only_1_class_count += events_per_day.count(1)
            consecutive_penalty += self.penaltyConsecutiveEvents(events_per_timeslot_per_day)

        if debug:   
            print("DBG::penaltySingleEventAndConcutiveEvents()::consecutive_penalty:: " + str(consecutive_penalty))
            print("DBG::penaltySingleEventAndConcutiveEvents()::only_1_class_count:: " + str(only_1_class_count))
        return only_1_class_count

    # Soft constraint part -> Count the number of consecutive class blocks within each day
    # +events_per_timeslot_per_day -> matrix with a row for each day. The row is a boolean list which represents if
    # the student is (or not) attending an event in that timeslot. 
    def penaltyConsecutiveEvents(self, events_per_timeslot_per_day):
        penalty = 0
        for events_in_day in events_per_timeslot_per_day:
            day_consecutive_count = 0
            for is_attending in events_in_day:
                if is_attending:
                    day_consecutive_count += 1
                    if (day_consecutive_count >= 3):
                        penalty += 1
                else:
                    day_consecutive_count = 0
        return penalty

    # Soft Constraint
    # Count the number of occurrences of a student attending an event in the last timeslot of the day (number of attendees of each 
    # event that takes place in the last timeslot of each day)
    def penaltyEndOfDayEvent(self, debug=False):
        penalty = 0
        for event_num in range(len(self.solution)):
            if (self.solution[event_num] % ProblemData.num_events_per_day in range(ProblemData.num_events_per_day - ProblemData.num_rooms, ProblemData.num_events_per_day)):
                penalty += ProblemData.events[event_num].num_attendees
        if debug:
            print("DBG::penaltyEndOfDayEvent():: " + str(penalty))
        return penalty

    def getNeighborStates(self):
        neighbor_states = []
        timeslot_identifier_index = 0
        for timeslot_identifier in self.solution:
            for i in range(0, ProblemData.NUM_TIMESLOTS * ProblemData.num_rooms):
                if i not in self.solution:  # Avoiding creating invalid solutions (with repeated timeslot identifiers to improve performance)
                    neighbor_state = list(self.solution)
                    neighbor_state[timeslot_identifier_index] = i
                    neighbor_states.append(Solution(neighbor_state))
            timeslot_identifier_index += 1
        return neighbor_states
