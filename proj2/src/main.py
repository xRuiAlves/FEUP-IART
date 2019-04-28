import sys

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

    print("\nGenerating a random generation . . .")
    gen = Generation()

    print("Starting to genetic algorith . . .")
    best = gen.getBest()
    while not best.isOptimal():
        print("Generation no. {}, best fitness={}.".format(gen.number, best.fitness))
        gen = gen.getNextGeneration()
        best = gen.getBest()

    print("\nFound optimal in generation no. {}.\nSolution: {}.\n".format(gen.number, best))




# Entry point
main()