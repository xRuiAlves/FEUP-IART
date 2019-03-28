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


def calculateWeightedBP(state):
    piece = state.specialPiece
    x = piece.x
    yStart = piece.y + piece.length
    yEnd = state.exitY
    count = 0
    for p in state.listOfPieces:
        if p.inRange(x, yStart, 1, yEnd - yStart):
            free = False
            for extremityX, extremityY, dx, dy in piece.getExtremities():
                if state.isEmpty(extremityX + dx, extremityY + dy):
                    count += 1
                    free = True
                    break
            
            if not free:
                count += 2
    return count


def greedyWeightedBP(stateOne, stateTwo):
    return (calculateWeightedBP(stateOne) + stateOne.getDistanceToEnd()) < (calculateWeightedBP(stateTwo) + stateTwo.getDistanceToEnd())


def aStarWeightedBP(stateOne, stateTwo):
    return (len(stateOne.movements) + calculateWeightedBP(stateOne)
            ) < (len(stateTwo.movements) + calculateWeightedBP(stateTwo))
