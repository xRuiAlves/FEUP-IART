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
    
    print("\nGenerating initial population . . .\n")

    gen = generatePopulation(50, print_progress=True)

    print("\nStarting Genetic algorithm . . .\n")

    best = gen.getBest()

    while best.fitness != 1:
        if (gen.number > maximum_generation_number):
            print("\nMaximum generation number reached. Aborting.")
            print("Best obtained solution:\n{}".format(best))
            print("\nNumber of generated solutions: {}".format(gen.number * ProblemData.POPULATION_SIZE))
            return
        print("Generation no. {}: ".format(gen.number), end="")
        print(best)
        gen = gen.getNextGeneration()
        best = gen.getBest()

    print("\nFound optimal solution in generation {}: {}".format(gen.number, best))
    print("\nNumber of generated solutions: {}".format(gen.number * ProblemData.POPULATION_SIZE))
    return

def hillClimbing():
    print("\nStarting Hill Climbing algorithm . . .\n")

    iteration_number = 1
    num_explored_states = 0
    solution = generateSolution()
    while not solution.isOptimal():
        old_fitness = solution.fitness
        print("Iteration no. {}: {}".format(iteration_number, solution))
        neighbor_states = solution.getNeighborStates()
        num_explored_states += len(neighbor_states)
        solution = max(neighbor_states, key=lambda solution: solution.fitness)
        new_fitness = solution.fitness

        if new_fitness <= old_fitness:
            print("\nCould not improve solution, local maximum reached.\n")    
            print("Best obtained solution (in {} iterations): {}".format(iteration_number, solution))
            print("Number of explored states: {}".format(num_explored_states))
            return

        iteration_number += 1

    print("\nFound optimal solution in iteration {}: {}".format(iteration_number, solution))
    print("Number of explored states: {}".format(num_explored_states))
    return

def simulatedAnnealing():
    print("\nStarting Simulated Annealing algorithm . . .\n")

    iteration_number = 1
    num_explored_states = 0
    solution = generateSolution()
    best_obtained_solution = solution
    annealing_prob = ProblemData.ANNEALING_INITIAL_PROB
    while not solution.isOptimal():
        old_fitness = solution.fitness
        print("Iteration no. {}: {}".format(iteration_number, solution))

        neighbor_states = solution.getNeighborStates()
        num_explored_states += len(neighbor_states)

        if (random.random() < annealing_prob):
            solution = neighbor_states[random.randint(0, len(neighbor_states) - 1)]
        else:
            solution = max(neighbor_states, key=lambda solution: solution.fitness)
        
        new_fitness = solution.fitness

        if (new_fitness > best_obtained_solution.fitness):
            best_obtained_solution = solution

        if annealing_prob <= 0 and new_fitness <= old_fitness:
            print("\nCould not further improve solution (local maximum reached with temperature equal to 0 in iteration no. {}).\n". format(iteration_number))  
            print("Local minimum solution: {}\nBest obtained solution: {}".format(solution, best_obtained_solution))
            print("Number of explored states: {}".format(num_explored_states))
            return

        iteration_number += 1
        annealing_prob -= ProblemData.ANNEALING_PROB_STEP

    print("\nFound optimal solution in iteration {}: {}".format(iteration_number, solution))
    print("Number of explored states: {}".format(num_explored_states))
    return

# Entry point
main()