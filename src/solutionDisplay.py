from graphics import *
from gameState import stateFromString
from search import breathSearch, depthSearch, progressiveDepth

windowWidth = 801
windowHeight = 801
pieceWidth = 100
specialPieceColor = color_rgb(200, 40, 40)
wallColor = color_rgb(139, 69, 19)
fixedBlockColor = color_rgb(30, 30, 30)
backgroundColor = color_rgb(150, 150, 150)

tempState = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooxxGG')

pieceColors = [
    color_rgb(190, 180, 180),
    color_rgb(180, 190, 180),
    color_rgb(180, 180, 190),
    color_rgb(190, 190, 180),
    color_rgb(180, 190, 190),
    color_rgb(190, 180, 190)
]

def drawWalls(window):
    points = [
        Point(0, 0),
        Point(8*pieceWidth, pieceWidth),

        Point(0, 7*pieceWidth),
        Point(8*pieceWidth, 8*pieceWidth),

        Point(0, pieceWidth),
        Point(pieceWidth, 7*pieceWidth),

        Point(7*pieceWidth, pieceWidth),
        Point(8*pieceWidth, 3*pieceWidth),

        Point(7*pieceWidth, 4*pieceWidth),
        Point(8*pieceWidth, 7*pieceWidth)
    ]

    for i in range(len(points)//2):
        wall = Rectangle(points[2*i], points[2*i + 1])
        wall.setFill(wallColor)
        wall.draw(window)

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
    model.draw(window)

def drawFixedBlocks(blocks, window):
    for block in blocks:
        p1 = Point((block[0] + 1)*pieceWidth, (block[1] + 1)*pieceWidth)
        p2 = Point((block[0] + 2)*pieceWidth, (block[1] + 2)*pieceWidth)
        model = Rectangle(p1, p2)
        model.setFill(fixedBlockColor)
        model.draw(window)


def initWindow():
    window = GraphWin("Unblock Me", windowWidth, windowHeight)
    window.setBackground(backgroundColor)
    return window

def drawState(state):
    window = initWindow()
    drawWalls(window)
    drawFixedBlocks(state.fixedBlocks, window)
    for index, piece in enumerate(state.listOfPieces):
        drawPiece(piece, index, window)
    window.getMouse()  # waits for mouse click input
    window.close()

drawState(tempState)
