from functools import partial
from solutionDisplay import drawSolution, drawSingleState
from gameState import stateFromString
from puzzles import easyPuzzles, mediumPuzzles, hardPuzzles, longPuzzles
from search import breadthSearch, depthSearch, progressiveDepth, informedSearch
from heuristics import greedyBlockingPieces, aStarBlockingPieces, greedyWeightedBlockingPieces, aStarWeightedBlockingPieces


class Menu:
    def __init__(
            self,
            title,
            optionNames=[],
            optionFunctions=[],
            isMainMenu=False):
        self.title = title
        self.optionNames = optionNames
        self.optionFunctions = optionFunctions
        self.optionNames.append("Exit" if isMainMenu else "Back")

    def display(self):
        while True:
            print()
            print("-" * (12 + len(self.title)))
            print("----- " + self.title + " -----\n")
            for i in range(len(self.optionNames)):
                print(str(i + 1) + ". " + self.optionNames[i])
            if (self.getOption()):
                return

    def getOption(self):
        while True:
            try:
                opt = int(input("\nEnter an option: "))
                print()
                if (opt >= 1 and opt < len(self.optionNames)):
                    self.optionFunctions[opt - 1]()
                    return
                elif (opt == len(self.optionNames)):
                    return True
                self.printErrMsg()
            except ValueError:
                self.printErrMsg()

    def printErrMsg(self):
        print("Invalid option. Please enter an option between 1 and " +
              str(len(self.optionNames)))


def getYesOrNo(msg=""):
    while True:
        ans = input(msg + " (Y/n): ").upper()
        if (ans in ["Y", "N"]):
            return (ans == "Y")


def puzzleChoice(puzzles):
    while True:
        try:
            puzzleNumber = int(
                input("Enter the puzzle number (between 1 and " + str(len(puzzles)) + "): "))
            if (puzzleNumber < 1 or puzzleNumber > len(puzzles)):
                print(
                    "Invalid puzzle number. Please enter a puzzle number between 1 and " + str(len(puzzles)))
                continue

            puzzle = stateFromString(list(puzzles.values())[puzzleNumber - 1])
            drawSingleState(puzzle)
            getAlgorithmChoice(puzzle, puzzleNumber)

            return
        except ValueError:
            print(
                "Invalid puzzle number. Please enter a puzzle number between 1 and " + str(len(puzzles)))


def getAlgorithmChoice(puzzle, puzzleNumber=None):
    algorithmsMenu = Menu("Choose Algorithm" + ((" for Puzzle no. " + str(puzzleNumber)) if puzzleNumber else ""),
                          [
                              "DFS",
                              "BFS",
                              "Iterative Deepening",
                              "Greedy Search H1",
                              "A* Search H1",
                              "Greedy Search H2",
                              "A* Search H2"
                          ],
                          [
                              partial(performAlgorithm, puzzle, depthSearch),
                              partial(performAlgorithm, puzzle, breadthSearch),
                              partial(performAlgorithm, puzzle, progressiveDepth),
                              partial(performAlgorithm, puzzle, informedSearch, heuristic=greedyBlockingPieces),
                              partial(performAlgorithm, puzzle, informedSearch, heuristic=aStarBlockingPieces),
                              partial(performAlgorithm, puzzle, informedSearch, heuristic=greedyWeightedBlockingPieces),
                              partial(performAlgorithm, puzzle, informedSearch, heuristic=aStarWeightedBlockingPieces)
                          ]
                          ).display()


def performAlgorithm(puzzle, algorithm, heuristic=None):
    puzzle.ordering = heuristic
        
    res = algorithm(puzzle)
    if res is None:
        print("Failed to find solution")
    else:
        print(res)
        drawSolution(res.getSolution())

def readPuzzleFromFile():
    while True:
        filename = input("Enter the filename: ")
        try:
            file = open(filename , "r")
        except IOError:
            print("File was not found.\n")
            continue
        puzzleText = file.readline()
        if (len(puzzleText) != 36):
            print("Invalid file content")
            continue
        puzzle = stateFromString(puzzleText)
        drawSingleState(puzzle)
        getAlgorithmChoice(puzzle)
        return


mainMenu = Menu("Unblock Me",
                [
                    "Easy Puzzles",
                    "Medium Puzzles",
                    "Hard Puzzles",
                    "Long Puzzles",
                    "Read Puzzle from file"
                ],
                [
                    partial(puzzleChoice, easyPuzzles),
                    partial(puzzleChoice, mediumPuzzles),
                    partial(puzzleChoice, hardPuzzles),
                    partial(puzzleChoice, longPuzzles),
                    readPuzzleFromFile
                ],
                isMainMenu=True
                ).display()
