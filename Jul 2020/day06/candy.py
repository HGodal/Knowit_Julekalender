import numpy as np

numElves = 127
candyList = np.genfromtxt('godteri.txt', delimiter=',', dtype=int)

for i in range(1, len(candyList)):
    if candyList[:-i].sum() % numElves == 0:
        print(f'Number of candies: {candyList[:-i].sum() // numElves}')
        break
