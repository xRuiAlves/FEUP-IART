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


def calculateWeightedBlockingPieces(state):
    piece = state.specialPiece
    x = piece.x
    yStart = piece.y + piece.length
    yEnd = state.exitY
    count = 0
    for p in state.listOfPieces:
        if p.inRange(x, yStart, 1, yEnd - yStart):
            count += 2
            for extremityX, extremityY, dx, dy in piece.getExtremities():
                if state.isEmpty(extremityX + dx, extremityY + dy):
                    count -= 1
                    break
    return count


def greedyWeightedBlockingPieces(stateOne, stateTwo):
    return (calculateWeightedBlockingPieces(stateOne) + stateOne.getDistanceToEnd()) < (calculateWeightedBlockingPieces(stateTwo) + stateTwo.getDistanceToEnd())


def aStarWeightedBlockingPieces(stateOne, stateTwo):
    return (len(stateOne.movements) + calculateWeightedBlockingPieces(stateOne)
            ) < (len(stateTwo.movements) + calculateWeightedBlockingPieces(stateTwo))
