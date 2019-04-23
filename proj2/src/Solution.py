import random
from ProblemData import ProblemData

NUM_DAYS = 5
NUM_TIMESLOTS_PER_DAY = 9
NUM_TIMESLOTS = NUM_DAYS * NUM_TIMESLOTS_PER_DAY


# TODO: Discuss
# After understanding the problem, the best way to represent a solution is an array with the events that are going to take place in each timeslot for each room.
# e.g. if there were 2 days with 2 timeslots each, 4 timeslots total
# if there were 3 rooms, there could be 12 events taking place in total (4 timeslots * 3 rooms)

class Solution:
    def __init__(self, solution=[]):
        self.solution = solution
        if (len(self.solution) == 0):
            self.randomize()

    def randomize(self):
        self.solution = [random.randint(0, ProblemData.num_events - 1) for i in range(NUM_TIMESLOTS * ProblemData.num_rooms)]

    def __str__(self):
        return "{}".format(self.solution)
