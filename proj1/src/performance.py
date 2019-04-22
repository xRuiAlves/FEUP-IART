import numpy as np
import matplotlib.pyplot as plt
import json

from gameState import stateFromString
from search import breadthSearch, depthSearch, progressiveDepth, informedSearch
from heuristics import greedyBlockingPieces, aStarBlockingPieces, greedyWeightedBlockingPieces, aStarWeightedBlockingPieces
from puzzles import easyPuzzles, mediumPuzzles, hardPuzzles, longPuzzles
from sys import argv


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


def extractData(statistics, alg, field):
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
        executionData = extractData(statistics, alg, field)
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


algGroups = {
    'all': [
        ('breadth', breadthSearch, None),
        ('depth', depthSearch, None),
        ('p-depth', progressiveDepth, None),
        ('greedy-bpieces', informedSearch, greedyBlockingPieces),
        ('a*-bpieces', informedSearch, aStarBlockingPieces),
        ('greedy-wbpieces', informedSearch, greedyWeightedBlockingPieces),
        ('a*-wbpieces', informedSearch, aStarWeightedBlockingPieces),
    ],

    'medium': [
        ('breadth', breadthSearch, None),
        ('depth', depthSearch, None),
        ('greedy-bpieces', informedSearch, greedyBlockingPieces),
        ('a*-bpieces', informedSearch, aStarBlockingPieces),
        ('greedy-wbpieces', informedSearch, greedyWeightedBlockingPieces),
        ('a*-wbpieces', informedSearch, aStarWeightedBlockingPieces),
    ],

    'fast': [
        ('depth', depthSearch, None),
        ('greedy-bpieces', informedSearch, greedyBlockingPieces),
        ('a*-bpieces', informedSearch, aStarBlockingPieces),
        ('greedy-wbpieces', informedSearch, greedyWeightedBlockingPieces),
        ('a*-wbpieces', informedSearch, aStarWeightedBlockingPieces),
    ]
}

puzzles = {
    'easy': easyPuzzles, 
    'medium': mediumPuzzles, 
    'hard': hardPuzzles, 
    'long': longPuzzles
}


def getData(puzzleIdentifier, algorithmIdentifier):
    puzzlesToBeAnalysed = puzzles[puzzleIdentifier]
    algs = algGroups[algorithmIdentifier]
    statistics = {}

    for puzzleId in puzzlesToBeAnalysed:
        print(puzzleId)
        statistics[puzzleId] = getStats(puzzlesToBeAnalysed[puzzleId], algs)

    with open('../data/' + puzzleIdentifier + '.json', 'w') as outfile:
        json.dump(statistics, outfile)


def buildGraph(puzzleIdentifier, statistics):
    createGrapth(
        statistics,
        'executionTime',
        'Execution Time (s)',
        'Execution Time (' + puzzleIdentifier + ')',
        barWidth=0.1,
        save=True,
        saveName='executionTime-' + puzzleIdentifier)

    createGrapth(
        statistics,
        'expandedNodes',
        'Expanded Nodes',
        'Expanded Nodes (' + puzzleIdentifier + ')',
        barWidth=0.1,
        save=True,
        saveName='expandedNodes-' + puzzleIdentifier)

    createGrapth(
        statistics,
        'answerLength',
        'Answer Length',
        'Answer Length (' + puzzleIdentifier + ')',
        barWidth=0.1,
        save=True,
        saveName='answerLength-' + puzzleIdentifier)

if len(argv) == 2:
    name = argv[1]
    with open('../data/' + name + '.json') as f:
        data = json.load(f)
        buildGraph(name, data)
elif (len(argv) == 3):
    getData(argv[1], argv[2])
else:
    print('Usage: python performance.py <puzzles> <algs>')
