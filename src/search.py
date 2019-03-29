from queue import Queue, PriorityQueue
from sys import maxsize
from stats import Stats


def breadthSearch(ini):
    stats = Stats()
    states = Queue()
    states.put(ini)

    searchedStates = set()

    stats.startTimer()
    while not states.empty():
        stateToAnalyze = states.get()

        if stateToAnalyze in searchedStates:
            stats.nodeSkipped()
            continue

        searchedStates.add(stateToAnalyze)
        stats.nodeExpanded()

        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                stats.nodeSkipped()
                continue

            if nextState.isFinal():
                stats.endTimer()
                return stats.setState(nextState)
            states.put(nextState)


def depthSearch(ini, maxDepth=maxsize):
    stats = Stats()
    states = [ini]
    searchedStates = set()

    stats.startTimer()
    while not (len(states) == 0):
        stateToAnalyze = states.pop()

        if stateToAnalyze in searchedStates:
            stats.nodeSkipped()
            continue

        searchedStates.add(stateToAnalyze)

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


def pSearchStep(ini, stats, maxDepth):
    states = [ini]
    searchedStates = set()

    while not (len(states) == 0):
        stateToAnalyze = states.pop()

        if (stateToAnalyze, stateToAnalyze.depth()) in searchedStates:
            stats.nodeSkipped()
            continue

        if stateToAnalyze.isFinal():
            stats.endTimer()
            return stats.setState(stateToAnalyze)

        searchedStates.add((stateToAnalyze, stateToAnalyze.depth()))

        stats.nodeExpanded()
        if stateToAnalyze.depth() >= maxDepth:
            continue

        for nextState in stateToAnalyze.getAllStates():
            if (nextState, nextState.depth()) in searchedStates:
                stats.nodeSkipped()
                continue
            states.append(nextState)


def progressiveDepth(ini):
    stats = Stats()
    sol = None
    depth = 0

    stats.startTimer()
    while sol is None:
        depth += 1
        sol = pSearchStep(ini, stats, depth)

    return sol


def informedSearch(ini):
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

        stats.nodeExpanded()
        for nextState in stateToAnalyze.getAllStates():
            if nextState in searchedStates:
                stats.nodeSkipped()
                continue
            states.put(nextState)
