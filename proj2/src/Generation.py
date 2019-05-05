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

    def getTotalFitness(self):
        sum = 0
        for solution in self.population:
            sum += solution.fitness
        return sum

    def hasOptimal(self):
        return self.getBest().fitness == 1

    def performTournament(self):
        tournament_sample = [self.population[random.randint(0, ProblemData.POPULATION_SIZE-1)] for i in range(ProblemData.TOURNAMENT_SIZE)] 
        return self.getBest(tournament_sample)

    def getNextGeneration(self):
        # Compute probability of each solution being selected
        total_fitness = self.getTotalFitness()
        
        # Selection process for next generation parents
        # TODO: como proceder se todos tiverem 0 fitness?
        selected = []
        if (total_fitness != 0):
            probabilities = []
            for solution in self.population:
                probabilities.append(solution.fitness / total_fitness)

            for i in range(ProblemData.POPULATION_SIZE):
                r = random.random()
                index = -1
                while(r > 0):
                    index += 1
                    r -= probabilities[index]
                selected.append(self.population[index])
        else:
            for i in range(ProblemData.POPULATION_SIZE):
                index = random.randint(0, len(self.population)-1)
                selected.append(self.population[index])

        # Crossover parents to generate new generation
        new_population = []

        # Maintain elites (if existant)
        if (ProblemData.ELITISM_FACTOR > 0):
            new_population = self.getBestN(ProblemData.ELITISM_FACTOR)

        while len(new_population) < ProblemData.POPULATION_SIZE:
            parent1 = selected[random.randint(0, len(selected) - 1)]
            parent2 = selected[random.randint(0, len(selected) - 1)]
            crossover_children = Solution.crossover(parent1, parent2)
            crossover_children[0].mutate()
            crossover_children[1].mutate()
            new_population.append(crossover_children[0])
            new_population.append(crossover_children[1])

        # When the population size is an odd number, one extra child was generated. Remove it.
        new_population = new_population[0:ProblemData.POPULATION_SIZE]
        
        return Generation(new_population, number=self.number+1)
