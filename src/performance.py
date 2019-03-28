import numpy as np
import matplotlib.pyplot as plt

from gameState import stateFromString
from search import breadthSearch, depthSearch, progressiveDepth, informedSearch
from heuristics import greedyBlockingPieces, aStarBlockingPieces
from puzzles import easyPuzzles, mediumPuzzles, hardPuzzles, longPuzzles


def calculate(initialState,
              algorithm,
              ordering,
              times=3,
              statistics=['executionTime', 'expandedNodes', 'answerLength']):
    averages = {}
    for stat in statistics:
        averages[stat] = 0

    for i in range(times):
        initialState.ordering = ordering
        res = algorithm(initialState)
        for stat in statistics:
            averages[stat] += getattr(res, stat)

    for stat in statistics:
        averages[stat] /= times

    return averages


def getStats(puzzleString, algorithms):
    ini = stateFromString(puzzleString)
    results = {}
    for name, function, ordering in algorithms:
        results[name] = calculate(ini, function, ordering)

    return results


def getData(statistics, alg, field):
    data = []
    for puzzleId in statistics:
        stats = statistics[puzzleId]
        data.append(stats[alg][field])

    return data


def createGrapth(
        statistics,
        field,
        ylabel,
        title,
        save=False,
        saveName=None,
        barWidth=0.3):
    n_puzzles = len(statistics)
    algs = list(next(iter(statistics.values())).keys())
    n_alg = len(algs)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_puzzles)
    opacity = 0.8

    for alg_index in range(n_alg):
        alg = algs[alg_index]
        executionData = getData(statistics, alg, field)
        rects1 = ax.bar(index + (alg_index + 1) * barWidth, executionData,
                        barWidth,
                        alpha=opacity,
                        label=alg)

    plt.xlabel('Puzzles')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(index + ((n_alg - 1) / 2 + 1) *
               barWidth, statistics.keys(), rotation=90)

    fig.tight_layout()

    plt.legend()
    if save:
        if saveName is None:
            plt.savefig("../graphics/" + field + ".png")
        else:
            plt.savefig("../graphics/" + saveName + ".png")
    else:
        plt.show()


allAlgorithms = [
    ('breadth', breadthSearch, None),
    ('depth', depthSearch, None),
    ('p-depth', progressiveDepth, None),
    ('greedy-bpieces', informedSearch, greedyBlockingPieces),
    ('a*-bpieces', informedSearch, aStarBlockingPieces),
]

fastAlgorithms = [
    ('depth', depthSearch, None),
    ('greedy-bpieces', informedSearch, greedyBlockingPieces),
    ('a*-bpieces', informedSearch, aStarBlockingPieces),
]

statistics = {}

for puzzleId in easyPuzzles:
    print(puzzleId)
    statistics[puzzleId] = getStats(easyPuzzles[puzzleId], allAlgorithms)

createGrapth(
    statistics,
    'executionTime',
    'Execution Time (s)',
    'Execution time in easy puzzles',
    barWidth=0.1,
    save=True,
    saveName='executionTimeEasy')

createGrapth(
    statistics,
    'expandedNodes',
    'Expanded Nodes',
    'Expanded nodes in easy puzzles',
    barWidth=0.1,
    save=True,
    saveName='expandedNodesEasy')

createGrapth(
    statistics,
    'answerLength',
    'Answer Length',
    'Answer length in easy puzzles',
    barWidth=0.1,
    save=True,
    saveName='answerLengthEasy')

statistics = {}

for puzzleDict in [mediumPuzzles, hardPuzzles, longPuzzles]:
    for puzzleId in puzzleDict:
        print(puzzleId)
        statistics[puzzleId] = getStats(puzzleDict[puzzleId], fastAlgorithms)

createGrapth(
    statistics,
    'executionTime',
    'Execution Time (s)',
    'Execution Time by Puzzle',
    barWidth=0.1,
    save=True)

createGrapth(
    statistics,
    'expandedNodes',
    'Expanded Nodes',
    'Expanded Nodes by Puzzle',
    barWidth=0.1,
    save=True)

createGrapth(
    statistics,
    'answerLength',
    'Answer Length',
    'Answer Length by Puzzle',
    barWidth=0.1,
    save=True)