import numpy as np
import matplotlib.pyplot as plt

from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth, informedSearch
from heuristics import greedyBlockingPieces, aStarBlockingPieces


def getStats(puzzleString):
    ini = stateFromString(puzzleString)
    results = {}
    results['breadth'] = breathSearch(ini, saveStates=True)
    results['depth'] = depthSearch(ini)
    results['p-depth'] = progressiveDepth(ini, saveStates=True)
    ini.ordering = greedyBlockingPieces
    results['greedy-bpieces'] = informedSearch(ini)
    ini.ordering = aStarBlockingPieces
    results['a*-bpieces'] = informedSearch(ini)
    return results


def getData(statistics, alg, field):
    data = []
    for puzzleId in statistics:
        stats = statistics[puzzleId]
        data.append(getattr(stats[alg], field))

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
            plt.savefig(saveName)
    else:
        plt.show()
    pass


puzzles = {
    'easy-a': 'BBBoFoooooFoAADoFoooDoooooEoooooECCC',
    'easy-b': 'BBBooxFooooHFAAooHGoooooGDDEEEoooooo',
    'easy-c': 'BBBooxFooooHFAAooHGoooooGDDDEEoooooo',
    'easy-d': 'BBooGooEooGooEAAGooEoCCooFoooooFDDDo',
    'easy-e': 'BBoooooGxDDooGAAIooHooIooHEEFFoooooo',
    'easy-f': 'oxCCDDoooooJoGAAoJoGoIEEoHoIoooHFFFo',
    'easy-g': 'oxCCCooooGoooAAGooooFDDxooFoooooFooo',
    'easy-h': 'oICCDDHIooKoHxAAKoHEEJFFoooJoooGGGoo',
    # 'medium-10-a': 'oooxoooooHoIEAAHoIEFCCCooFGoooDDGooo',
    # 'medium-10-b': 'ooooGoDoooGIDAAFHIooEFHoooEFBBoCCCoo',
    # 'medium-10-c': 'GBBBoxGoDDoIAAoHoIoooHEEoooHooooFFoo',
    # 'medium-10-d': 'FBBoKoFoIoKLAAIooLooJCCoGHJoooGHDDEE',
    # 'medium-10-e': 'ooIBBBooIJoLoAAJKLoxDDKoHoEEooHFFFxo',
    # 'medium-10-f': 'ooGHBBFoGHIJFAAoIJoCCooooooxoxoooooo',
    # 'medium-10-g': 'HoIBBoHoIJoKHAAJoKCCoooooxEEoxGGoooo',
    # 'medium-10-h': 'EoooooEooHBBEAAHoIoFGCCIoFGooJDDDooJ',
    # 'medium-10-i': 'ooHoBBooHCCCFAAoIJFGDDIJoGooIxoooooo',
    # 'medium-10-j': 'ooBBBxooJoKLAAJoKLIDDxooIFFoooGGHHoo',
    # 'hard-10-a': 'BBHoKLooHoKLAAIooMoGICCMFGoJDDFEEJoo',
    # 'hard-10-b': 'BBJoooHoJxLxHAAKLoEEoKoMoIFFoMoIGGoo',
    # 'hard-10-c': 'oIBBLMoICCLMAAoKooHDDKooHoJxoxGGJooo',
    # 'hard-10-d': 'oHBBoxoHIooLAAIooLGoIDDoGEEJKooFFJKo',
    # 'hard-10-e': 'oGBBoKoGHooKAAHIoKFoHICCFDDoJooEEoJo',
    # 'hard-10-f': 'oIBBxooIDDoLAAJooLHoJEEoHFFoKoGGGoKo',
    # 'hard-10-g': 'IJBBCCIJDDxoIAALoooooLFFooKGGMHHKooM',
    # 'hard-10-h': 'BBIooLoHIoxLoHAAKMDDoJKMGooJEEGFFFoo',
    # 'hard-10-i': 'BBCCLooxEELMAAJooMIoJFFMIGGKoooHHKoo',
    # 'hard-10-j': 'GBBoKLGHooKLGHIAAMCCIJoMoooJDDEEFFoo',
}

statistics = {}

for puzzleId in puzzles:
    print(puzzleId)
    statistics[puzzleId] = getStats(puzzles[puzzleId])

createGrapth(
    statistics,
    'executionTime',
    'Execution Time (s)',
    '',
    barWidth=0.1,
    save=True)
createGrapth(
    statistics,
    'expandedNodes',
    'Expanded Nodes',
    '',
    barWidth=0.1,
    save=True)
createGrapth(
    statistics,
    'answerLength',
    'Answer Length',
    '',
    barWidth=0.1,
    save=True)
