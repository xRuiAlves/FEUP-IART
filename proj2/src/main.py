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

    # Generate a random solution (temporary)
    print("\nGenerating solution until solution is valid . . .\n")
    solution_is_valid = False
    while not solution_is_valid:
        s = Solution()
        solution_is_valid = s.isValid()

    print("\nGenerated Valid Solution:")
    print(s)
    print()

    penalty = s.penalty()
    print("\nSoft constaints penalty: " + str(penalty))

    print("\n-----------\n")
    print("Generating a random generation . . .")
    gen = Generation()
    print(gen)


# Entry point
main()