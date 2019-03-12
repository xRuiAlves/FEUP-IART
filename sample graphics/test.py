from graphics import *

window_width = 800
window_height = 800
piece_width = 80
window = GraphWin("test", window_width, window_height)
window.setBackground(color_rgb(160, 160, 160))

def drawWalls():
    wall_color = color_rgb(139,69,19)
    points = []

    points.append(Point(0,0))
    points.append(Point(window_width -1 , piece_width))
    points.append(Point(0, window_height - 1))
    points.append(Point(window_width - 1, window_height - piece_width - 1))
    points.append(Point(0, piece_width))
    points.append(Point(piece_width, window_height - piece_width - 1))
    points.append(Point(window_width - piece_width - 1, piece_width))
    points.append(Point(window_width - 1, 3*piece_width - 1))
    points.append(Point(window_width - piece_width - 1, 4*piece_width))
    points.append(Point(window_width - 1, piece_width + 8*piece_width - 1))

    for i in range(len(points)//2):
        w = Rectangle(points[2*i], points[2*i + 1])
        w.setFill(wall_color)
        w.draw(window)

def drawSpecialPiece():
    piece_color = color_rgb(170,35,35)
    p1 = Point(1*piece_width, 3*piece_width)
    p2 = Point(4*piece_width - 1, 4*piece_width - 1)
    piece = Rectangle(p1, p2)
    piece.setFill(piece_color)
    piece.draw(window)

def drawPieces():
    piece_color = color_rgb(170, 170, 30)
    points = []

    points.append(Point(1*piece_width, 1*piece_width))
    points.append(Point(4*piece_width - 1, 2*piece_width - 1))
    points.append(Point(4*piece_width - 1, 1*piece_width))
    points.append(Point(5*piece_width - 1, 4*piece_width - 1))
    points.append(Point(5*piece_width - 1, 3*piece_width))
    points.append(Point(6*piece_width - 1, 5*piece_width - 1))
    points.append(Point(4*piece_width, 5*piece_width - 1))
    points.append(Point(7*piece_width - 1, 6*piece_width - 1))
    points.append(Point(7*piece_width - 1, 1*piece_width))
    points.append(Point(8*piece_width - 1, 5*piece_width - 1))
    points.append(Point(8*piece_width - 1, 3*piece_width))
    points.append(Point(9*piece_width - 1, 7*piece_width - 1))
    points.append(Point(2*piece_width - 1, 7*piece_width))
    points.append(Point(3*piece_width - 1, 9*piece_width - 1))
    points.append(Point(5*piece_width - 1, 7*piece_width))
    points.append(Point(6*piece_width - 1, 9*piece_width - 1))

    for i in range(len(points)//2):
        piece = Rectangle(points[2*i], points[2*i + 1])
        piece.setFill(piece_color)
        piece.draw(window)


drawWalls()
drawSpecialPiece()
drawPieces()
window.getMouse()  # waits for mouse click input
window.close()
