from queue import Queue, PriorityQueue
from .state import StaticStateUpdater
from sys import maxsize


def breadthSearch(ini, debug=False):
    states = Queue()
    states.put(ini)
    searchedStates = []

    while True:
        stateToAnalyze = states.get()

        if stateToAnalyze in searchedStates:
            continue
        searchedStates.append(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze) + ' - ', end="")

        for nextState in stateToAnalyze.getAllStates():
            if debug:
                print(str(nextState), end=" ", flush=True)
            if nextState.isFinal():
                if debug:
                    print()
                return nextState
            states.put(nextState)
        if debug:
            print()


def depthSearch(ini, maxDepth=maxsize, debug=False):
    return recursiveDS(ini, 0, [], maxDepth, debug)


def recursiveDS(stateToAnalyze, depth,
                prevStates, maxDepth, debug=False):
    if stateToAnalyze.isFinal():
        return stateToAnalyze

    if debug:
        print(str(depth) + " - " +
              str(stateToAnalyze) + " " + str(stateToAnalyze.transitions))

    if depth >= maxDepth:
        return None

    nextPStates = prevStates.copy()
    nextPStates.append(stateToAnalyze)
    for nextState in stateToAnalyze.getAllStates():
        res = None
        if nextState not in prevStates:
            res = recursiveDS(nextState, depth +
                              1, nextPStates, maxDepth, debug)
        if res is not None:
            return res

    return None


def progressiveDepth(ini, deb=False):
    sol = None
    depth = 0
    while sol is None:
        depth += 1
        sol = depthSearch(ini, maxDepth=depth, debug=deb)

    return sol


def informedSearch(ini, debug=False):
    states = PriorityQueue()
    states.put(ini)
    searchedStates = []
    while True:
        stateToAnalyze = states.get()

        if stateToAnalyze in searchedStates:
            if debug:
                print(str(stateToAnalyze) + " already analized")
            continue
        searchedStates.append(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze) + ' - ', end="")

        for nextState in stateToAnalyze.getAllStates():
            if debug:
                print(str(nextState), end=" ", flush=True)
            if nextState.isFinal():
                if debug:
                    print()
                return nextState
            states.put(nextState)
        if debug:
            print()
