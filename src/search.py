from queue import Queue, PriorityQueue
from sys import maxsize
from stats import Stats


def breathSearch(ini, debug=False):
    stats = Stats()
    states = Queue()
    states.put(ini)
    searchedStates = []

    stats.startTimer()
    while True:
        stateToAnalyze = states.get()

        if stateToAnalyze in searchedStates:
            continue
        searchedStates.append(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)
            states.put(nextState)


def depthSearch(ini, maxDepth=maxsize, debug=False):
    stats = Stats()
    states = [ini]
    searchedStates = []

    stats.startTimer()
    while True:
        if len(states) == 0:
            return None

        stateToAnalyze = states.pop()

        if stateToAnalyze in searchedStates:
            continue

        searchedStates.append(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)

            if stateToAnalyze.depth() < maxDepth:
                states.append(nextState)


def pSearchStep(ini, stats, maxDepth=maxsize, debug=False):
    states = [ini]
    searchedStates = []

    while True:
        if len(states) == 0:
            return None

        stateToAnalyze = states.pop()
        if stateToAnalyze in searchedStates:
            continue

        searchedStates.append(stateToAnalyze)
        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)

            if nextState.depth() < maxDepth:
                states.append(nextState)


def progressiveDepth(ini, deb=False):
    stats = Stats()
    sol = None
    depth = 0

    stats.startTimer()
    while sol is None:
        depth += 1
        sol = pSearchStep(ini, stats, maxDepth=depth, debug=deb)

    return sol


def informedSearch(ini, debug=False):
    stats = Stats()
    states = PriorityQueue()
    states.put(ini)
    searchedStates = []

    stats.startTimer()
    while True:
        stateToAnalyze = states.get()

        if stateToAnalyze in searchedStates:
            continue
        searchedStates.append(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)
            states.put(nextState)
