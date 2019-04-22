import sys

from Student import Student
from Event import Event
from Room import Room
from FileReader import FileReader
from Solution import Solution

def main():
    if (len(sys.argv) < 2):
        sys.stderr.write("Error: Not enough arguments.\n")
        sys.stderr.write("usage: " + sys.argv[0] + " <input_file>\n")
        return 1
        
    input_file = sys.argv[1]
    f = FileReader()
    f.readFile(input_file)

    # Generate a random solution (temporary)
    print("\nRandom solution example:")
    s = Solution(len(f.events), len(f.rooms))
    print(s)



# Entry point
main()