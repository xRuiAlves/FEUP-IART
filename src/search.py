from queue import Queue, PriorityQueue
from sys import maxsize
from stats import Stats


def breathSearch(ini, debug=False, saveStates=True):
    stats = Stats()
    states = Queue()
    states.put(ini)

    searchedStates = set()

    stats.startTimer()
    while True:
        if states.empty():
            return None

        stateToAnalyze = states.get()

        if debug:
            print(str(stateToAnalyze))

        if saveStates:
            searchedStates.add(stateToAnalyze)

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if saveStates and nextState in searchedStates:
                stats.nodeSkipped()
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)
            states.put(nextState)


def depthSearch(ini, maxDepth=maxsize, debug=False):
    stats = Stats()
    states = [ini]
    searchedStates = set()

    stats.startTimer()
    while True:
        if len(states) == 0:
            return None

        stateToAnalyze = states.pop()

        if stateToAnalyze in searchedStates:
            stats.nodeSkipped()
            continue

        searchedStates.add(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                stats.nodeSkipped()
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)

            if stateToAnalyze.depth() < maxDepth:
                states.append(nextState)


def pSearchStep(ini, stats, saveStates, debug, maxDepth):
    states = [ini]
    searchedStates = set()

    while True:
        if len(states) == 0:
            return None

        stateToAnalyze = states.pop()

        if saveStates and (stateToAnalyze, stateToAnalyze.depth()) in searchedStates:
            stats.nodeSkipped()
            continue

        if stateToAnalyze.isFinal():
            stats.endTimer()
            return stats.setState(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        if saveStates:
            searchedStates.add((stateToAnalyze, stateToAnalyze.depth()))

        stats.nodeExpanded()
        if stateToAnalyze.depth() >= maxDepth:
            continue

        for nextState in stateToAnalyze.getAllStates():

            if saveStates and (nextState, nextState.depth()) in searchedStates:
                stats.nodeSkipped()
                continue

            states.append(nextState)


def progressiveDepth(ini, debug=False, saveStates=True):
    stats = Stats()
    sol = None
    depth = 0

    stats.startTimer()
    while sol is None:
        depth += 1
        sol = pSearchStep(ini, stats, saveStates, debug, depth)

    return sol


def informedSearch(ini, debug=False):
    stats = Stats()
    states = PriorityQueue()
    states.put(ini)
    searchedStates = set()

    stats.startTimer()
    while True:
        stateToAnalyze = states.get()

        if stateToAnalyze.isFinal():
            stats.endTimer()
            return stats.setState(stateToAnalyze)

        if stateToAnalyze in searchedStates:
            stats.nodeSkipped()
            continue
        searchedStates.add(stateToAnalyze)

        if debug:
            print(str(stateToAnalyze))

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                stats.nodeSkipped()
                continue
            states.put(nextState)
