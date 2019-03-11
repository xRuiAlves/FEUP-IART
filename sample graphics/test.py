from graphics import *

window_width = 800
window_height = 800
piece_width = 80
window = GraphWin("test", window_width, window_height)
window.setBackground(color_rgb(160, 160, 160))

def drawWalls():
    wall_color = color_rgb(139,69,19)

    p1 = Point(0,0)
    p2 = Point(window_width -1 , piece_width)
    p3 = Point(0, window_height - 1)
    p4 = Point(window_width - 1, window_height - piece_width - 1)
    p5 = Point(0, piece_width)
    p6 = Point(piece_width, window_height - piece_width - 1)
    p7 = Point(window_width - piece_width - 1, piece_width)
    p8 = Point(window_width - 1, 3*piece_width - 1)
    p9 = Point(window_width - piece_width - 1, 4*piece_width)
    p10 = Point(window_width - 1, piece_width + 8*piece_width - 1)

    w1 = Rectangle(p1, p2)
    w2 = Rectangle(p3, p4)
    w3 = Rectangle(p5, p6)
    w4 = Rectangle(p7, p8)
    w5 = Rectangle(p9, p10)
    w1.setFill(wall_color)
    w2.setFill(wall_color)
    w3.setFill(wall_color)
    w4.setFill(wall_color)
    w5.setFill(wall_color)
    w1.draw(window)
    w2.draw(window)
    w3.draw(window)
    w4.draw(window)
    w5.draw(window)

def drawSpecialPiece():
    piece_color = color_rgb(170,35,35)
    p1 = Point(piece_width, 3*piece_width)
    p2 = Point(4*piece_width - 1, 4*piece_width - 1)
    piece = Rectangle(p1, p2)
    piece.setFill(piece_color)
    piece.draw(window)


drawWalls()
drawSpecialPiece()
window.getMouse()  # waits for mouse click input
window.close()
