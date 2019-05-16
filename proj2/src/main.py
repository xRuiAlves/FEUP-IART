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
    input_file = sys.argv[1]
    try:
        ProblemData.readFile(input_file)
    except:
        sys.stderr.write("Error: Failed file parsing: Invalid input file.\n")
        return 2

    print("\n")

    maximum_generation_number = 200
    num_experiments = 10
    ProblemData.MUTATION_PROB = 0.05

    for i in range(10):
        times = 0
        num_solutions = 0
        penn = 0
        for i in range(num_experiments):
            gen = generatePopulation(50, print_progress=False)

            best = gen.getBest()
            num_solutions += ProblemData.POPULATION_SIZE

            t1 = time.time()
            while best.fitness != 1:
                if (gen.number > maximum_generation_number):
                    break
            
                gen = gen.getNextGeneration()
                best = gen.getBest()
                num_solutions += ProblemData.POPULATION_SIZE
            t2 = time.time()
            times += (t2 - t1)
            penn += best.penalty
            ProblemData.MUTATION_PROB += 0.025

        print("{:.1f},{:.4f},{}".format(penn/num_experiments, times/num_experiments, num_solutions//num_experiments))


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
geneticAlgorithm()