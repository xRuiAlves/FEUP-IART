import random
from Solution import Solution
from ProblemData import ProblemData

class Generation:
    def __init__(self, population=None, number=1):
        self.number = number
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

    def getBestN(self, n):
        return sorted(self.population, key=lambda solution: solution.fitness, reverse=True)[:n]

    def getBest(self, solutions_list=None):
        return max(solutions_list if solutions_list is not None else self.population, key=lambda solution: solution.fitness)

    def hasOptimal(self):
        return self.getBest().fitness == 0

    def performTournament(self):
        tournament_sample = [self.population[random.randint(0, ProblemData.POPULATION_SIZE-1)] for i in range(ProblemData.TOURNAMENT_SIZE)] 
        return self.getBest(tournament_sample)

    def getNextGeneration(self):
        new_population = []
        if (ProblemData.ELITISM_FACTOR > 0):
            new_population = self.getBestN(ProblemData.ELITISM_FACTOR)
            
        while (len(new_population) < ProblemData.POPULATION_SIZE):
            new_population.append(self.generateSolution())
            
        return Generation(new_population,number=self.number+1)

    def generateSolution(self):
        parent1 = self.performTournament()
        parent2 = self.performTournament()
        child = parent1.crossover(parent2)
        child.mutate()
        return child