from time import time


class Stats:
    def __init__(self):
        self.gameState = None
        self.answerLength = 0
        self.expandedNodes = 0
        self.startTime = 0
        self.endTime = 0
        self.executionTime = 0
        self.skippedStates = 0
        self.finished = False

    def startTimer(self):
        self.startTime = time()

    def endTimer(self):
        self.endTime = time()
        self.executionTime = self.endTime - self.startTime

    def nodeExpanded(self):
        self.expandedNodes += 1

    def nodeSkipped(self):
        self.skippedStates += 1

    def setState(self, gameState):
        self.finished = True
        self.gameState = gameState
        self.answerLength = len(gameState.previousStates)
        return self

    def __str__(self):
        return "Answer length: {}\nNumber of nodes Expanded: {}\nNumber of nodes Skipped: {}\nTime taken: {}s\n".format(
            self.answerLength, self.expandedNodes, self.skippedStates, self.executionTime)

    def getSolution(self):
        return self.gameState.previousStates + [self.gameState]
