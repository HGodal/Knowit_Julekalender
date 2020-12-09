import numpy as np
import pandas as pd

allLines = []


def addLines(matrix):
    for line in matrix:
        allLines.append(line)
        allLines.append(line[::-1])


df = np.array(pd.read_csv('matrix.txt', sep=r'\s*', engine='python',
                          header=None).iloc[:, 1:-1])

for i in range(2):
    addLines(np.sum(df, axis=i))
    for j in range(-999, 1000):
        addLines(str(np.diag(df, k=j).sum()).split(" "))
    df = np.fliplr(df)

allWords = pd.read_csv('wordlist.txt', sep='\n', header=None)[0].tolist()

for line in allLines:
    for word in allWords:
        if word in line:
            allWords.remove(word)

print(f'Words missing from matrix: {sorted(allWords)}')
