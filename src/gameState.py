from math import sqrt, floor
from copy import deepcopy, copy
from piece import Piece


class GameState:
    def __init__(
            self,
            emptyMatrix,
            listOfPieces,
            specialPiece,
            exitX=None,
            exitY=None,
            ordering=None,
            previousStates=[],
            emptySymbol=' ',
            wallSymbol='x'):

        self.emptyMatrix = emptyMatrix
        self.listOfPieces = listOfPieces
        self.previousStates = previousStates
        self.specialPiece = specialPiece
        self.emptySymbol = emptySymbol
        self.wallSymbol = wallSymbol
        self.ordering = ordering
        self.exitX = 2 if exitX is None else exitX
        self.exitY = len(self.emptyMatrix[0]) - 1 if exitY is None else exitY

    def isFinal(self):
        return self.specialPiece.onTop(self.exitX, self.exitY)

    def getAllStates(self):
        nextStates = []
        for pieceNumber in range(len(self.listOfPieces)):
            piece = self.listOfPieces[pieceNumber]
            for extremityX, extremityY, dx, dy in piece.getExtremities():
                movX = dx
                movY = dy
                while self.isEmpty(extremityX + movX, extremityY + movY):

                    eMatrix = deepcopy(self.emptyMatrix)
                    lPieces = copy(self.listOfPieces)

                    piece.applyEmpty(movX if movX != 0 else movY, eMatrix)
                    nPiece = piece.newPiece(movX, movY)
                    nPiece.applyOccupied(eMatrix)
                    lPieces[pieceNumber] = nPiece

                    sp = lPieces[pieceNumber] if piece is self.specialPiece else self.specialPiece
                    prevState = copy(self.previousStates).append(self)
                    nextStates.append(GameState(eMatrix, lPieces,
                                                sp, self.exitX, self.exitY,
                                                self.ordering, prevState,
                                                self.emptySymbol,
                                                self.wallSymbol))

                    movX += dx
                    movY += dy

        return nextStates

    def isEmpty(self, x, y):
        return x >= 0 and y >= 0 \
            and x < len(self.emptyMatrix) \
            and y < len(self.emptyMatrix[0]) \
            and self.emptyMatrix[x][y]

    def depth(self):
        return len(self.previousState)

    def __str__(self):
        characterMap = [[self.emptySymbol] *
                        len(self.emptyMatrix[0]) for x in range(len(self.emptyMatrix))]

        for x in range(len(self.emptyMatrix)):
            for y in range(len(self.emptyMatrix[0])):
                if not self.emptyMatrix[x][y]:
                    characterMap[x][y] = self.wallSymbol

        for piece in self.listOfPieces:
            piece.apply(characterMap)

        strRep = '\n'
        for line, emptyLine in zip(characterMap, self.emptyMatrix):
            for cell in line:
                strRep += cell
                strRep += ' '
            strRep += '\t'
            for emptyCell in emptyLine:
                if emptyCell:
                    strRep += ' '
                    strRep += ' '
                else:
                    strRep += 'O'
                    strRep += ' '

            strRep += '\n'
        return strRep

    def __eq__(self, value):
        return str(self) == str(value)

    def __lt__(self, other):
        if self.ordering is None:
            return len(self.previousStates) < len(other.previousStates)
        else:
            return self.ordering(self, other)


def stateFromString(
        stateStr,
        emptySymbol='o',
        specialSymbol='A',
        wallSymbol='x'):
    n = int(floor(sqrt(len(stateStr))))
    emptyMatrix = [[True] * n for x in range(n)]
    pieces = {}
    specialPiece = None

    for pos in range(len(stateStr)):
        cell = stateStr[pos]
        x = floor(pos / n)
        y = pos % n

        if cell == emptySymbol:
            continue

        if cell == wallSymbol:
            emptyMatrix[x][y] = False
            continue

        if cell in pieces:
            pieces[cell].addCell(x, y)
        elif cell == specialSymbol:
            specialPiece = Piece(cell, x, y)
            pieces[cell] = specialPiece
        else:
            pieces[cell] = Piece(cell, x, y)

        emptyMatrix[x][y] = False

    if specialPiece is None:
        raise 'No special piece'

    return GameState(emptyMatrix, list(pieces.values()), specialPiece)
