import sys
import time
import random
from copy import copy
from collections import deque
from math import floor

from Student import Student
from Event import Event
from Room import Room
from ProblemData import ProblemData
from Solution import Solution
from Generation import Generation

class Room:
    def __init__(self, room):
        self.room = room
        self.size = self.room.size
        self.reset()

    def reserveSlot(self, attendees, slotsOccupied):
        if len(self.freeTimeslots) == 0:
            return None
        for slot in self.freeTimeslots:
            collisions = sum([i*j for (i, j) in zip(slotsOccupied[slot], attendees)])
            if collisions == 0:
                slotsOccupied[slot] = [i+j for (i, j) in zip(slotsOccupied[slot], attendees)]
                self.usedTimeslots.add(slot)
                self.freeTimeslots.remove(slot)
                return slot*ProblemData.num_rooms + self.room.id 
        return None

    def reset(self):
        self.usedTimeslots = set()
        self.freeTimeslots = set(random.sample(range(0,ProblemData.NUM_TIMESLOTS), ProblemData.NUM_TIMESLOTS))

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

    def getRoom(self, event, slotsOccupied):
        roomNumber = None
        randomRooms = random.sample(self.rooms, len(self.rooms))
        for room in randomRooms:
            if room.size >= event.num_attendees:
                roomNumber = room.reserveSlot(event.attendees, slotsOccupied)
            if roomNumber is not None:
                return roomNumber
        return roomNumber

    def getRoomRecursively(self, event, slotsOccupied):
        roomNumber = self.getRoom(event, slotsOccupied)
        if roomNumber is not None:
            return roomNumber
        childrenNodes = deque(copy(self.children))
        while len(childrenNodes) > 0:
            node = childrenNodes.popleft()
            roomNumber = node.getRoom(event, slotsOccupied)
            if roomNumber is not None:
                return roomNumber
            for child in node.children:
                childrenNodes.append(child)

        # if roomNumber is None:
        #     raise BaseException('Implement random when not found')
        return roomNumber
    
    def reset(self):
        for room in self.rooms:
            room.reset()

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
        c = copy(sol)
        c.append(0)
        sols.append(c)
        c = copy(sol)
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

def createSlotMatrix():
    return [[0] * ProblemData.num_students for i in range(ProblemData.NUM_TIMESLOTS)]

def randomizeNone(solution):
    taken = set(solution)

    for i in range(len(solution)):
        s = solution[i]
        if s is not None:
            continue
        r = random.randint(0, ProblemData.NUM_TIMESLOTS * ProblemData.num_rooms - 1)
        while (len(taken & set([r])) != 0):
            r = random.randint(0, ProblemData.NUM_TIMESLOTS * ProblemData.num_rooms - 1)
        solution[i] = r



def generateSolution():
    roomsByFeatures = buildRoomTree()
    slotsOccupied = createSlotMatrix()
    events = ProblemData.events
    solution = []

    for event in events:
        slot = roomsByFeatures[tuple(event.features)].getRoomRecursively(event, slotsOccupied)
        solution.append(slot)
    
    randomizeNone(solution)
    return solution

def generatePopulation(size, print_progress=False):
    roomsByFeatures = buildRoomTree()
    events = ProblemData.events
    population = []

    for i in range(size):
        if(print_progress):
            printProgress(i/size)
        slotsOccupied = createSlotMatrix()
        solution = []
        for event in events:
            slot = roomsByFeatures[tuple(event.features)].getRoomRecursively(event, slotsOccupied)
            solution.append(slot)
        randomizeNone(solution)
        if i != size - 1:
            for key in roomsByFeatures:
                roomsByFeatures[key].reset()
        population.append(Solution(solution))
    if (print_progress):
        printProgress(1, carriage_return=False)
    return Generation(population)

def printProgress(progress, carriage_return=True):
    progress_bar_total_size = 20

    progress_bar_size = floor(progress * progress_bar_total_size)

    print("[" + progress_bar_size * "#" + (progress_bar_total_size - progress_bar_size) * "." + "], " + str(int(progress*100)) + "%", end=("\r" if carriage_return else "\n"))
