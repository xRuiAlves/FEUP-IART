import numpy as np
import matplotlib.pyplot as plt

from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth


def getStats(puzzleString):
    ini = stateFromString(puzzleString)
    results = {}
    results['breadth'] = breathSearch(ini, saveStates=True)
    results['depth'] = depthSearch(ini)
    results['p-depth'] = progressiveDepth(ini, saveStates=True)
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
    plt.xticks(index + ((n_alg-1)/2 + 1) * barWidth, statistics.keys(), rotation=90)

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
    'super-easy-a': 'BBBoFoooooFoAADoFoooDoooooEoooooECCC',
    'super-easy-b': 'BBBooxFooooHFAAooHGoooooGDDEEEoooooo',
    'super-easy-c': 'BBBooxFooooHFAAooHGoooooGDDDEEoooooo',
    'super-easy-d': 'BBooGooEooGooEAAGooEoCCooFoooooFDDDo',
    'super-easy-e': 'BBoooooGxDDooGAAIooHooIooHEEFFoooooo',
    'super-easy-f': 'oxCCDDoooooJoGAAoJoGoIEEoHoIoooHFFFo',
    'super-easy-g': 'oxCCCooooGoooAAGooooFDDxooFoooooFooo',
    'super-easy-h': 'oICCDDHIooKoHxAAKoHEEJFFoooJoooGGGoo',
    # 'easy-10-a': 'oooxoooooHoIEAAHoIEFCCCooFGoooDDGooo',
    # 'easy-10-b': 'ooooGoDoooGIDAAFHIooEFHoooEFBBoCCCoo',
    # 'easy-10-c': 'GBBBoxGoDDoIAAoHoIoooHEEoooHooooFFoo',
    # 'easy-10-d': 'FBBoKoFoIoKLAAIooLooJCCoGHJoooGHDDEE',
    # 'easy-10-e': 'ooIBBBooIJoLoAAJKLoxDDKoHoEEooHFFFxo',
    # 'easy-10-f': 'ooGHBBFoGHIJFAAoIJoCCooooooxoxoooooo',
    # 'easy-10-g': 'HoIBBoHoIJoKHAAJoKCCoooooxEEoxGGoooo',
    # 'easy-10-h': 'EoooooEooHBBEAAHoIoFGCCIoFGooJDDDooJ',
    # 'easy-10-i': 'ooHoBBooHCCCFAAoIJFGDDIJoGooIxoooooo',
    # 'easy-10-j': 'ooBBBxooJoKLAAJoKLIDDxooIFFoooGGHHoo',
    # 'medium-10-a': 'BBHoKLooHoKLAAIooMoGICCMFGoJDDFEEJoo',
    # 'medium-10-b': 'BBJoooHoJxLxHAAKLoEEoKoMoIFFoMoIGGoo',
    # 'medium-10-c': 'oIBBLMoICCLMAAoKooHDDKooHoJxoxGGJooo',
    # 'medium-10-d': 'oHBBoxoHIooLAAIooLGoIDDoGEEJKooFFJKo',
    # 'medium-10-e': 'oGBBoKoGHooKAAHIoKFoHICCFDDoJooEEoJo',
    # 'medium-10-f': 'oIBBxooIDDoLAAJooLHoJEEoHFFoKoGGGoKo',
    # 'medium-10-g': 'IJBBCCIJDDxoIAALoooooLFFooKGGMHHKooM',
    # 'medium-10-h': 'BBIooLoHIoxLoHAAKMDDoJKMGooJEEGFFFoo',
    # 'medium-10-i': 'BBCCLooxEELMAAJooMIoJFFMIGGKoooHHKoo',
    # 'medium-10-j': 'GBBoKLGHooKLGHIAAMCCIJoMoooJDDEEFFoo',
}

statistics = {}

for puzzleId in puzzles:
    print(puzzleId)
    statistics[puzzleId] = getStats(puzzles[puzzleId])

createGrapth(statistics, 'executionTime', 'Execution Time (s)', '', barWidth=0.1, save=True)
createGrapth(statistics, 'expandedNodes', 'Expanded Nodes', '', barWidth=0.1, save=True)
createGrapth(statistics, 'answerLength', 'Answer Length', '', barWidth=0.1, save=True)
