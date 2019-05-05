import sys
import time
import random
from copy import copy
from collections import deque

from Student import Student
from Event import Event
from Room import Room
from ProblemData import ProblemData
from Solution import Solution
from Generation import Generation

class Room:
    def __init__(self, room):
        self.occupancy = 0
        self.room = room
        self.usedTimeslots =  random.sample(range(0,ProblemData.NUM_TIMESLOTS), ProblemData.NUM_TIMESLOTS)

    def reserveSlot(self):
        if self.occupancy >= ProblemData.NUM_TIMESLOTS:
            return None
        self.occupancy += 1
        reservedSlot = self.usedTimeslots[self.occupancy - 1] * ProblemData.num_rooms + self.room.id
        if reservedSlot is None:
            raise BaseException("Coding error")
        return reservedSlot

    def __str__(self):
        return "{} - {}".format(self.occupancy, self.room)

class RoomNode:
    def __init__(self, key, room=None):
        if room is None:
            self.rooms = []
        else:
            self.rooms = [Room(room)]
        self.key = key
        self.children = []

    def append(self, room):
        self.rooms.append(Room(room))

    def addChild(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.key)

    def getRoom(self):
        roomNumber = None
        randomRooms = random.sample(self.rooms, len(self.rooms))
        for room in randomRooms:
            roomNumber = room.reserveSlot()
            if roomNumber is not None:
                return roomNumber
        return roomNumber

    def getRoomRecursively(self):
        roomNumber = self.getRoom()
        if roomNumber is not None:
            return roomNumber
        childrenNodes = deque(copy(self.children))
        while len(childrenNodes) > 0:
            node = childrenNodes.popleft()
            roomNumber = node.getRoom()
            if roomNumber is not None:
                return roomNumber
            for child in node.children:
                childrenNodes.append(child)
        return roomNumber
    
    def reset(self):
        for room in self.rooms:
            room.occupancy = 0

def oneStepAway(firstKey, secondKey):
    differences = 0
    for firstElem, secondElem in zip(firstKey, secondKey):
        if firstElem ==  1 and secondElem == 0:
            return False
        if firstElem != secondElem:
            differences += 1
        if differences > 1:
            return False
    return differences == 1

def generateCombination(size):
    if size == 1:
        return [[0], [1]]
    sols = []
    for sol in generateCombination(size - 1):
        c = sol.copy()
        c.append(0)
        sols.append(c)
        c = sol.copy()
        c.append(1)
        sols.append(c)
    return sols

def buildRoomTree():
    roomsByFeatures = {}
    nFeatures = ProblemData.num_features
    for key in generateCombination(nFeatures):
        roomsByFeatures[tuple(key)] = RoomNode(tuple(key))
    for room in ProblemData.rooms:
        key = tuple(room.features)
        if key not in roomsByFeatures:
            print("Error in code")
        else:
            roomsByFeatures[key].append(room)

    for firstKey in roomsByFeatures:
        for secondKey in roomsByFeatures:
            if firstKey != secondKey and oneStepAway(firstKey, secondKey):
                roomsByFeatures[firstKey].addChild(roomsByFeatures[secondKey])

    return roomsByFeatures

def generateSolution():
    roomsByFeatures = buildRoomTree()
    events = ProblemData.events
    solution = []

    for event in events:
        solution.append(roomsByFeatures[tuple(event.features)].getRoomRecursively())
    return Solution(solution)

def generatePopulation(size):
    roomsByFeatures = buildRoomTree()
    events = ProblemData.events
    population = []

    for i in range(size):
        solution = []
        for event in events:
            solution.append(roomsByFeatures[tuple(event.features)].getRoomRecursively())

        if i != size - 1:
            for key in roomsByFeatures:
                roomsByFeatures[key].reset()
        population.append(Solution(solution))
    return Generation(population)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        sys.stderr.write("Error: Not enough arguments.\n")
        sys.stderr.write("usage: " + sys.argv[0] + " <input_file>\n")
        sys.exit(-1)
        
    input_file = sys.argv[1]
    try:
        ProblemData.readFile(input_file)
    except:
        sys.stderr.write("Error: Failed file parsing: Invalid input file.\n")
        sys.exit(-2)

    print(generatePopulation(100))
