import sys

from Student import Student
from Event import Event
from Room import Room
from ProblemData import ProblemData
from Solution import Solution

def main():
    if (len(sys.argv) < 2):
        sys.stderr.write("Error: Not enough arguments.\n")
        sys.stderr.write("usage: " + sys.argv[0] + " <input_file>\n")
        return 1
        
    input_file = sys.argv[1]
    ProblemData.readFile(input_file)

    # Generate a random solution (temporary)
    print("\nRandom solution example:")
    s = Solution()
    print(s)
    validity = s.isValid()
    print("\nIs valid: " + str(validity))

    penalty = s.penaltyEndOfDayClass()
    print("Soft constaints penalty: " + str(penalty))



# Entry point
main()