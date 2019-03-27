from search.search import breathSearch, depthSearch
from search.search import progressiveDepth, informedSearch
from copy import deepcopy


class PuzzleState:
    def __init__(self, puzzle_matrix, transitions=[], ordering=None):
        self.matrix = puzzle_matrix
        self.transitions = transitions
        self.ordering = ordering

    def getAllStates(self):
        zeroX, zeroY = self.getZeroPosition()
        offsets = {'botttom': (1, 0), 'right': (
            0, 1), 'top': (-1, 0), 'left': (0, -1)}

        states = []
        for mov in offsets:
            offX, offY = offsets[mov]
            x = zeroX + offX
            y = zeroY + offY

            if x < 0 or x >= len(self.matrix) or y < 0 or y >= len(
                    self.matrix[0]):
                continue

            newMatrix = deepcopy(self.matrix)
            newTransitions = deepcopy(self.transitions)

            newTransitions.append(mov)
            newMatrix[x][y] = 0
            newMatrix[zeroX][zeroY] = self.matrix[x][y]
            state = PuzzleState(newMatrix, newTransitions, self.ordering)
            states.append(state)

        return states

    def isFinal(self):
        nextCell = 0
        for line in self.matrix:
            for cell in line:
                if cell != nextCell:
                    return False
                nextCell += 1

        return True

    def getZeroPosition(self):
        for i, line in enumerate(self.matrix):
            for j, cell in enumerate(line):
                if cell == 0:
                    return (i, j)
        raise Exception("No Zero Found")

    def __str__(self):
        return str(self.matrix)

    def __eq__(self, value):
        for lineSelf, lineValue in zip(self.matrix, value.matrix):
            for s, v in zip(lineSelf, lineValue):
                if s != v:
                    return False
        return True

    def __lt__(self, other):
        if self.ordering is None:
            return len(self.transitions) < len(other.transitions)
        else:
            return self.ordering(self, other)


def greedyH1(stateOne, stateTwo):
    oneOutOrder = 0
    twoOutOrder = 0
    number = 0
    for lineOne, lineTwo in zip(
            stateOne.matrix, stateTwo.matrix):
        for one, two in zip(lineOne, lineTwo):
            if one != number:
                oneOutOrder += 1
            if two != number:
                twoOutOrder += 1

            number += 1

    return oneOutOrder < twoOutOrder


def aStarH1(stateOne, stateTwo):
    oneOutOrder = 0
    twoOutOrder = 0
    number = 0
    for lineOne, lineTwo in zip(
            stateOne.matrix, stateTwo.matrix):
        for one, two in zip(lineOne, lineTwo):
            if one != number:
                oneOutOrder += 1
            if two != number:
                twoOutOrder += 1

            number += 1

    return oneOutOrder + \
        len(stateOne.transitions) < twoOutOrder + len(stateTwo.transitions)


def greedyH2(stateOne, stateTwo):
    return h2(stateOne.matrix) < h2(stateTwo.matrix)


def aStarH2(stateOne, stateTwo):
    return h2(stateOne.matrix) + \
        len(stateOne.transitions) < h2(stateTwo.matrix) + \
        len(stateTwo.transitions)


def h2(state):
    nLines = len(state)
    nColumns = len(state[0])
    sum = 0

    for i in range(nLines):
        for j in range(nColumns):
            number = state[i][j]
            idealX = int(number / nLines)
            idealY = number % nLines
            sum += abs(idealX - i) + abs(idealY - j)
    return sum


puzzles = {
    0: [[1, 2, 3], [5, 0, 6], [4, 7, 8]],
    1: [[1, 3, 6], [5, 2, 0], [4, 7, 8]],
    2: [[1, 6, 2], [5, 7, 3], [0, 4, 8]],
    3: [[5, 1, 3, 4], [2, 0, 7, 8], [10, 6, 11, 12], [9, 12, 14, 15]]
}

for n in puzzles:
    print("Puzzle " + str(n))
    puzzle = puzzles[n]
    ini = PuzzleState(puzzle)

    # res = breathSearch(ini)
    # print("\tBreadth: " + str(res.transitions))

    # res = depthSearch(ini, maxDepth=10)
    # print("\tDepth: " + str(res.transitions))

    # res = progressiveDepth(ini)
    # print("\tProgressive Depth: " + str(res.transitions))

    ini = PuzzleState(puzzle, ordering=greedyH1)
    res = informedSearch(ini)
    print("\tGreedy H1: " + str(res.transitions))

    ini = PuzzleState(puzzle, ordering=aStarH1)
    res = informedSearch(ini)
    print("\tA* H1: " + str(res.transitions))

    ini = PuzzleState(puzzle, ordering=greedyH2)
    res = informedSearch(ini)
    print("\tGreedy H2: " + str(res.transitions))

    ini = PuzzleState(puzzle, ordering=aStarH2)
    res = informedSearch(ini)
    print("\tA* H2: " + str(res.transitions))

    print()
