import random
from Solution import Solution
from ProblemData import ProblemData

class Generation:
    def __init__(self, population=[]):
        self.population = population
        if (len(self.population) == 0):
            self.randomize()

    def randomize(self):
        for i in range(ProblemData.POPULATION_SIZE):
            self.population.append(Solution())

    def __str__(self):
        return "".join((str(solution) + "\n") for solution in self.population)