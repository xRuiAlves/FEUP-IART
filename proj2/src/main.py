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

    print("\nGenerating a random generation . . .\n")
    gen = Generation()
    best = gen.getBest()
    print(best)

    while best.fitness != 1:
        gen = gen.getNextGeneration()
        best = gen.getBest()
        print(best)

    print("Found solution in generation " + str(gen.number))



# Entry point
main()