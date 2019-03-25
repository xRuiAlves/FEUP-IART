from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth

ini = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooooGG')

print(ini)

res = breathSearch(ini, saveStates=True)
if res is not None:
    print("Breadth: " + str(res))
    # res.gameState.playGame()

res = depthSearch(ini)
if res is not None:
    print("Depth: " + str(res))
    # res.gameState.playGame()

res = progressiveDepth(ini, saveStates=True)
if res is not None:
    print("P-Depth: " + str(res))
    # res.gameState.playGame()
