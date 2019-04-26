import random
from Solution import Solution
from ProblemData import ProblemData

class Generation:
    def __init__(self, population=None):
        if (population  == None):
            self.population = []
            self.randomize()
        else:
            self.population = population

    def randomize(self):
        for i in range(ProblemData.POPULATION_SIZE):
            self.population.append(Solution())

    def __str__(self):
        return "".join((str(solution) + "\n") for solution in self.population)

    def getValidSolutions(self):
        return [solution for solution in self.population if solution.is_valid]