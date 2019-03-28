def calculateBlockingPieces(state):
    piece = state.specialPiece
    x = piece.x
    yStart = piece.y + piece.length
    yEnd = state.exitY
    count = 0
    for p in state.listOfPieces:
        if p.inRange(x, yStart, 1, yEnd - yStart):
            count += 1
    return count

def greedyBlockingPieces(stateOne, stateTwo):
    return (calculateBlockingPieces(stateOne) + stateOne.getDistanceToEnd()) < (calculateBlockingPieces(stateTwo) + stateTwo.getDistanceToEnd())

def aStarBlockingPieces(stateOne, stateTwo):
    return (len(stateOne.movements) + calculateBlockingPieces(stateOne)
            ) < (len(stateTwo.movements) + calculateBlockingPieces(stateTwo))
