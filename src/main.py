from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth

ini = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooooGG')

print(ini)

# res = breathSearch(ini)
# if res is not None:
#     print("Breadth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
#           .format(
#               res.gameState.movements,
#               res.answerLength,
#               res.expandedNodes,
#               res.executionTime))

res = depthSearch(ini, maxDepth=5)
if res is not None:
    print("Depth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
          .format(
              res.gameState.movements,
              res.answerLength,
              res.expandedNodes,
              res.executionTime))

# res = progressiveDepth(ini)
# if res is not None:
#     print("P-Depth: {}\n\t{} answer length\n\t{} nodes expanded\n\t{} seconds"
#           .format(
#               res.gameState.movements,
#               res.answerLength,
#               res.expandedNodes,
#               res.executionTime))
