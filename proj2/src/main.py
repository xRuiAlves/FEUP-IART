import sys
import time
import random

from Student import Student
from Event import Event
from Room import Room
from ProblemData import ProblemData
from Solution import Solution
from Generation import Generation
from populationGeneration import generateSolution, generatePopulation

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
    print()
    while True:
        try:
            maximum_generation_number = int(input("Please enter the maximum generation number: "))
            break
        except ValueError:
            continue
    
    print("\nStarting Genetic algorithm . . .\n")

    gen = generatePopulation(50)
    best = gen.getBest()

    while best.fitness != 1:
        if (gen.number > maximum_generation_number):
            print("\nMaximum generation number reached. Aborting.")
            print("Best obtained solution:")
            print(best)
            return
        print("Generation no. {}: ".format(gen.number), end="")
        print(best)
        gen = gen.getNextGeneration()
        best = gen.getBest()

    print("\nFound optimal solution in generation {}:".format(gen.number))
    print(best)
    return

def hillClimbing():
    print("\nStarting Hill Climbing algorithm . . .\n")

    solution = generateSolution()
    while not solution.isOptimal():
        old_fitness = solution.fitness
        print(solution)
        solution = solution.getBestNeighbor()
        new_fitness = solution.fitness

        if new_fitness <= old_fitness:
            print("\nCould not improve solution, local maximum reached.\n")    
            print("Best obtained solution:")
            print(solution)        
            return

    print("\nFound optimal solution:")
    print(solution)
    return

def simulatedAnnealing():
    print("\nStarting Simulated Annealing algorithm . . .\n")

    solution = generateSolution()
    best_obtained_solution = solution
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

        if (new_fitness > best_obtained_solution.fitness):
            best_obtained_solution = solution

        if annealing_prob <= 0 and new_fitness <= old_fitness:
            print("\nCould not further improve solution (local maximum reached with temperature equal to 0).\n")  
            print("Local minimum solution:")
            print(solution)
            print("Best obtained solution:")
            print(best_obtained_solution)      
            return

        annealing_prob -= ProblemData.ANNEALING_PROB_STEP

    print("\nFound optimal solution:")
    print(solution)
    return

# Entry point
main()