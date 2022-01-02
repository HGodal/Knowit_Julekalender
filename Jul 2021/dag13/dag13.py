import numpy as np


def valid_move(height, y, x, pipe):
    if x < 0 or x >= pipe.shape[1]:
        return False
    if y < 0 or y >= pipe.shape[0]:
        return False

    if pipe[y, x] > height:
        return False

    return True


def landed(height, y, x, pipe):
    if pipe[y, x]+1 == height:
        return True
    return False


flytt = open('moves.txt').read().splitlines()
pipe = np.zeros((9, 9))


for pakke in flytt[:]:
    x, y = 4, 4
    height = 250

    for retning in pakke:
        height -= 1
        if landed(height, x, y, pipe):
            break
        if retning == 'N':
            y_temp = y+1
            if valid_move(height, y_temp, x, pipe):
                y = y_temp
        elif retning == 'S':
            y_temp = y-1
            if valid_move(height, y_temp, x, pipe):
                y = y_temp
        elif retning == 'E':
            x_temp = x+1
            if valid_move(height, y, x_temp, pipe):
                x = x_temp
        elif retning == 'W':
            x_temp = x-1
            if valid_move(height, y, x_temp, pipe):
                x = x_temp

    pipe[y, x] += 1
print(pipe)
print(np.max(pipe))
