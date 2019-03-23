from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth

ini = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooooGG')

res = breathSearch(ini)
print("Breadth: ")
for state in res.previousStates:
    print(state)
print(res)

res = depthSearch(ini, maxDepth=10)
print("Depth: ")
for state in res.previousStates:
    print(state)
print(res)

res = progressiveDepth(ini)
print("Progressive Depth: ")
for state in res.previousStates:
    print(state)
print(res)
