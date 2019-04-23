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
    try:
        ProblemData.readFile(input_file)
    except:
        sys.stderr.write("Error: Failed file parsing: Invalid input file.\n")
        return 2

    # Generate a random solution (temporary)
    print("\nRandom solution example:")
    s = Solution()
    print(s)
    validity = s.isValid()
    print("\nIs valid: " + str(validity))

    if not validity:
        return 2

    penalty = s.penalty()
    print("Soft constaints penalty: " + str(penalty))



# Entry point
main()