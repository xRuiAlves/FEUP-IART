from search.search import breathSearch, depthSearch, progressiveDepth
from search.state import StaticStateUpdater


def fillOne(prevState, nextState):
    if prevState[0] == 4:
        return None
    nextState[0] = 4
    return nextState


def fillTwo(prevState, nextState):
    if prevState[1] == 3:
        return None
    nextState[1] = 3
    return nextState


def emptyOne(prevState, nextState):
    if prevState[0] == 0:
        return None
    nextState[0] = 0
    return nextState


def emptyTwo(prevState, nextState):
    if prevState[1] == 0:
        return None
    nextState[1] = 0
    return nextState


def emptyOneIntoTwo(prevState, nextState):
    if not (prevState[1] + prevState[0] <= 3 and
            prevState[0] > 0 and
            prevState[1] < 3):
        return None
    nextState[0] = 0
    nextState[1] = prevState[1] + prevState[0]
    return nextState


def emptyTwoIntoOne(prevState, nextState):
    if not (prevState[1] + prevState[0] <= 4 and
            prevState[1] > 0 and
            prevState[0] < 4):
        return None
    nextState[1] = 0
    nextState[0] = prevState[1] + prevState[0]
    return nextState


def fillOneWithTwo(prevState, nextState):
    if not (prevState[0] < 4 and
            prevState[1] > 0 and
            prevState[1] - (4 - prevState[0]) >= 0):
        return None
    nextState[1] = prevState[1] - (4 - prevState[0])
    nextState[0] = 4
    return nextState


def fillTwoWithOne(prevState, nextState):
    if not (prevState[1] < 3 and
            prevState[0] > 0 and
            prevState[0] - (3 - prevState[1]) >= 0):
        return None
    nextState[0] = prevState[0] - (3 - prevState[1])
    nextState[1] = 3
    return nextState


ramifications = [
    fillOne,
    fillTwo,
    fillOneWithTwo,
    fillTwoWithOne,
    emptyOneIntoTwo,
    emptyTwoIntoOne,
    emptyOne,
    emptyTwo
]

ini = StaticStateUpdater([0, 0], [2, 0], ramifications)

res = breathSearch(ini)
print("Breadth: " + str(res.transitions))
res = depthSearch(ini)
print("Depth: " + str(res.transitions))
res = progressiveDepth(ini)
print("Progressive Depth: " + str(res.transitions))
