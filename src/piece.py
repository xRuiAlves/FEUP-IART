class Piece:
    def __init__(self, id, x, y, direction=None, length=1):
        self.id = id
        self.x = x
        self.y = y
        self.direction = direction
        self.length = length

    def addCell(self, x, y):
        if self.direction is None:
            if x == self.x:
                self.direction = 'H'
                if self.y + self.length == y:
                    self.length += 1
            elif y == self.y:
                self.direction = 'V'
                if self.x + self.length == x:
                    self.length += 1

        elif self.direction == 'V':
            if self.x + self.length == x:
                self.length += 1

        elif self.direction == 'H':
            if self.y + self.length == y:
                self.length += 1

    def apply(self, mapMatrix):
        if self.direction == 'V':
            for x in range(self.length):
                mapMatrix[self.x + x][self.y] = self.id

        elif self.direction == 'H':
            for y in range(self.length):
                mapMatrix[self.x][self.y + y] = self.id

    def onTop(self, x, y):
        if self.direction == 'V':
            for posX in range(self.length):
                if x == posX + self.x and y == self.y:
                    return True

        elif self.direction == 'H':
            for posY in range(self.length):
                if x == self.x and y == posY + self.y:
                    return True

        return False

    def inRange(self, x, y, width, height):
        if self.direction == 'H':
            self.width = self.length
            self.height = 1
        else:
            self.width = 1
            self.height = self.length

        return self.x < x + width and self.x + \
            self.width > x and self.y < y + height and self.y + self.height > y

    def getExtremities(self):
        ex = []
        if self.direction == 'V':
            ex.append((self.x, self.y, -1, 0))
            ex.append((self.x + self.length - 1, self.y, 1, 0))
        elif self.direction == 'H':
            ex.append((self.x, self.y, 0, -1))
            ex.append((self.x, self.y + self.length - 1, 0, 1))

        return ex

    def newPiece(self, movX, movY):
        nPiece = Piece(self.id, self.x + movX,
                       self.y + movY, self.direction,
                       self.length)
        return nPiece

    def applyOccupied(self, emptyMatrix):
        if self.direction == 'V':
            for x in range(self.length):
                emptyMatrix[self.x + x][self.y] = False

        elif self.direction == 'H':
            for y in range(self.length):
                emptyMatrix[self.x][self.y + y] = False

    def applyEmpty(self, mov, emptyMatrix):
        absMov = abs(mov)
        if self.direction == 'V':
            if mov > 0:
                for x in range(absMov):
                    emptyMatrix[self.x + x][self.y] = True
            else:
                for x in range(absMov):
                    emptyMatrix[self.x + self.length - x - 1][self.y] = True
        elif self.direction == 'H':
            if mov > 0:
                for y in range(absMov):
                    emptyMatrix[self.x][self.y + y] = True
            else:
                for y in range(absMov):
                    emptyMatrix[self.x][self.y + self.length - y - 1] = True

    def __eq__(self, value):
        if value is Piece:
            return self.id == value.id \
                and self.x == value.x \
                and self.y == value.y \
                and self.length == value.length
        return False

    def __str__(self):
        return "{} : ({}, {}) {} {} ".format(
            self.id, self.x, self.y, self.direction, self.length)
