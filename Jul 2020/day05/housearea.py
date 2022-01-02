from operator import add
import numpy as np

directionDict = {
    'V': [-1, 0],
    'H': [1, 0],
    'O': [0, 1],
    'N': [0, -1]
}


def coordinate(direction):
    return directionDict[direction]


currentCoordinate = [0, 0]
with open("rute.txt") as f:
    for line in f:
        xCoor = np.zeros(len(line))
        yCoor = np.zeros(len(line))
        for i in range(len(line)):
            currentCoordinate = list(
                map(add, currentCoordinate, coordinate(line[i])))
            xCoor[i] = currentCoordinate[0]
            yCoor[i] = currentCoordinate[1]


def PolyArea(x, y):  # Shoelace area formula
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


print(PolyArea(xCoor, yCoor))
