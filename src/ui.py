from functools import partial

class Menu:
    def __init__(self, title, optionNames=[], optionFunctions=[]):
        self.title = title
        self.optionNames = optionNames + ["Exit"]
        self.optionFunctions = optionFunctions

    def display(self):
        while True:
            print()
            print("-" * (12 + len(self.title)))
            print("----- " + self.title + " -----\n")
            for i in range(len(self.optionNames)):
                print(str(i+1) + ". " + self.optionNames[i])
            if (self.getOption() == "Exit"):
                return


    def getOption(self):
        while True:
            try:
                opt = int(input("\nEnter an option: "))
                print()
                if (opt >= 1 and opt < len(self.optionNames)):
                    self.optionFunctions[opt-1]()
                    return
                elif (opt == len(self.optionNames)):
                    return "Exit"
                self.printErrMsg()
            except ValueError:
                self.printErrMsg()

    def printErrMsg(self):
        print("Invalid option. Please enter an option between 1 and " + str(len(self.optionNames)))

def getYesOrNo(msg=""):
    while True:
        ans = input(msg + " (Y/n): ").upper()
        if (ans in ["Y", "N"]):
            return (ans == "Y")

def puzzleChoise(puzzles=[]):
    print("Puzzles: ", end="")
    print(puzzles)
    while True:
        try:
            puzzleNumber = int(input("Enter the puzzle number (between 1 and " + str(len(puzzles)) + "): "))
            if (puzzleNumber < 1 or puzzleNumber > len(puzzles)):
                print("Invalid puzzle number. Please enter a puzzle number between 1 and " + str(len(puzzles)))
                continue
            
            print("\n\nTODO: COMPUTATIONS\n\n")

            displaySolution = getYesOrNo("Would you like to visualize the puzzle solution?")
            if (displaySolution):
                print("-> TODO: DISPLAY SOLUTION <-")

            displayCharts = getYesOrNo("Would you like to visualize the performance charts?")
            if (displayCharts):
                print("-> TODO: DISPLAY PERFORMANCE CHARTS <-")
            
            return
        except ValueError:
            print("Invalid puzzle number. Please enter a puzzle number between 1 and " + str(len(puzzles)))

mainMenu = Menu("Unblock Me", 
                [
                    "Easy Puzzles", 
                    "Medium Puzzles", 
                    "Hard Puzzles", 
                    "Very hard Puzzles"
                ], 
                [
                    partial(puzzleChoise, [1, 2]), 
                    partial(puzzleChoise, [3, 4]),  
                    partial(puzzleChoise, [5, 6]), 
                    partial(puzzleChoise, [7, 8])
                ]).display()
