from graphics import *
from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth
from time import sleep

windowWidth = 801
windowHeight = 801
pieceWidth = 100
pieceBorderWidth = 3
specialPieceColor = color_rgb(220, 43, 43)
wallColor = color_rgb(89, 44, 12)
fixedBlockColor = wallColor
backgroundColor = color_rgb(198, 185, 175)
animationSpeed = 0.350

pieceColors = [
    color_rgb(64, 75, 109),
    color_rgb(74, 75, 115),
    color_rgb(54, 85, 109),
    color_rgb(74, 92, 113),
    color_rgb(80, 77, 112),
    color_rgb(60, 90, 112),
    color_rgb(75, 80, 120),
    color_rgb(100, 77, 112),
    color_rgb(60, 110, 112),
    color_rgb(90, 102, 120)
]

def drawPiece(piece, pieceNum, window):
    if (piece.direction == "H"):
        p1 = Point((piece.y + 1)*pieceWidth, (piece.x + 1)*pieceWidth)
        p2 = Point((piece.y + piece.length + 1)*pieceWidth, (piece.x + 2)*pieceWidth)
    else:
        p1 = Point((piece.y + 1)*pieceWidth, (piece.x + 1)*pieceWidth)
        p2 = Point((piece.y + 2)*pieceWidth, (piece.x + piece.length + 1)*pieceWidth)
    model = Rectangle(p1, p2)
    if (piece.id == "A"):
        model.setFill(specialPieceColor)
    else:
        model.setFill(pieceColors[pieceNum % len(pieceColors)])
    model.setWidth(pieceBorderWidth)
    model.draw(window)

def drawFixedBlocks(blocks, window):
    for block in blocks:
        p1 = Point((block[0] + 1)*pieceWidth, (block[1] + 1)*pieceWidth)
        p2 = Point((block[0] + 2)*pieceWidth, (block[1] + 2)*pieceWidth)
        model = Rectangle(p1, p2)
        model.setFill(fixedBlockColor)
        model.draw(window)

def initWindow():
    window = GraphWin("Unblock Me", windowWidth, windowHeight, autoflush=False)
    window.setBackground(backgroundColor)
    return window

def cls(window):
    wall_p1 = Point(-1, -1)
    wall_p2 = Point(windowWidth, windowHeight)
    wall_model = Rectangle(wall_p1, wall_p2)
    wall_model.setFill(wallColor)
    wall_model.setWidth(0)
    wall_model.draw(window)

    background_p1 = Point(pieceWidth - 1, pieceWidth - 1)
    background_p2 = Point(7*pieceWidth + 1, 7*pieceWidth + 1)
    background_model = Rectangle(background_p1, background_p2)
    background_model.setFill(backgroundColor)
    background_model.setWidth(0)
    background_model.draw(window)

    door_p1 = Point(7*pieceWidth - 1, 3*pieceWidth - 1)
    door_p2 = Point(8*pieceWidth + 1, 4*pieceWidth + 1)
    door_model = Rectangle(door_p1, door_p2)
    door_model.setWidth(0)
    door_model.setFill(backgroundColor)
    door_model.draw(window)


def drawState(state, window):
    cls(window)
    drawFixedBlocks(state.fixedBlocks, window)
    for index, piece in enumerate(state.listOfPieces):
        drawPiece(piece, index, window)

def drawSolution(states):
    window = initWindow()
    for state in states:
        drawState(state, window)
        update(10)
        sleep(animationSpeed)
    window.getMouse()  # waits for mouse click input
    window.close()