import sys

from Student import Student
from Event import Event
from Room import Room
from FileReader import FileReader

def main():
    if (len(sys.argv) < 2):
        sys.stderr.write("Error: Not enough arguments.\n")
        sys.stderr.write("usage: " + sys.argv[0] + " <input_file>\n")
        return 1
        
    input_file = sys.argv[1]
    f = FileReader()
    f.readFile(input_file)


# Entry point
main()