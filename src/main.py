from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth

ini = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooxoGG')

print(ini)

# res = breathSearch(ini)
# if res is not None:
#     print("Breadth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
#           .format(
#               res.gameState.movements,
#               res.answerLength,
#               res.expandedNodes,
#               res.executionTime))
    # res.gameState.playGame()

res = depthSearch(ini)
if res is not None:
    print("Depth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
          .format(
              res.gameState.movements,
              res.answerLength,
              res.expandedNodes,
              res.executionTime))
    # res.gameState.playGame()

res = progressiveDepth(ini)
if res is not None:
    print("P-Depth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
          .format(
              res.gameState.movements,
              res.answerLength,
              res.expandedNodes,
              res.executionTime))
    # res.gameState.playGame()
