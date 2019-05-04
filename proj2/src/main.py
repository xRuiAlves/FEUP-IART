import sys
import time
import random

from Student import Student
from Event import Event
from Room import Room
from ProblemData import ProblemData
from Solution import Solution
from Generation import Generation

def main():
    if (len(sys.argv) < 2):
        sys.stderr.write("Error: Not enough arguments.\n")
        sys.stderr.write("usage: " + sys.argv[0] + " <input_file>\n")
        return 1
        
    input_file = sys.argv[1]
    try:
        ProblemData.readFile(input_file)
    except:
        sys.stderr.write("Error: Failed file parsing: Invalid input file.\n")
        return 2

    print("--------------------------------------")
    print("---  Timetable Scheduling Problem  ---")
    print("--------------------------------------\n")
    print("1. Genetic Algorithm")
    print("2. Hill Climbing")
    print("3. Simulated Annealing\n")

    while True:
        try:
            option = int(input("Choose the desired algorithm: "))
            if option in [1, 2, 3]:
                break
        except ValueError:
            continue
    
    t1 = time.time()

    if option == 1:
        geneticAlgorithm()
    elif option == 2:
        hillClimbing()
    elif option == 3:
        simulatedAnnealing()

    t2 = time.time()

    print("Execution time: {:.4f} seconds".format(t2-t1))

def geneticAlgorithm():
    print("\nStarting Genetic algorithm . . .\n")

    gen = Generation()
    best = gen.getBest()
    print(best)

    while best.fitness != 1:
        gen = gen.getNextGeneration()
        best = gen.getBest()
        print(best)

    print("\nFound solution in generation " + str(gen.number))
    return

def hillClimbing():
    print("\nStarting Hill Climbing algorithm . . .\n")

    solution = Solution()
    while not solution.isOptimal():
        old_fitness = solution.fitness
        print(solution)
        solution = solution.getBestNeighbor()
        new_fitness = solution.fitness

        if new_fitness <= old_fitness:
            print("\nCould not improve solution, local maximum reached.")        
            return

    print("\nFound optimal solution:")
    print(solution)
    return

def simulatedAnnealing():
    print("\nStarting Simulated Annealing algorithm . . .\n")

    solution = Solution()
    annealing_prob = ProblemData.ANNEALING_INITIAL_PROB
    while not solution.isOptimal():
        old_fitness = solution.fitness
        print(solution)

        if (random.random() < annealing_prob):
            neighbors = solution.getNeighborStates()
            solution = neighbors[random.randint(0, len(neighbors) - 1)]
        else:
            solution = solution.getBestNeighbor()
        
        new_fitness = solution.fitness

        if annealing_prob <= 0 and new_fitness <= old_fitness:
            print("\nCould not improve solution, local maximum reached.")        
            return

        annealing_prob -= ProblemData.ANNEALING_PROB_STEP

    print("\nFound optimal solution:")
    print(solution)
    return

# Entry point
main()