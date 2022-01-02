import numpy as np
import re


def gå_retning(rute, retning):
    ny_retning = ''

    if rute[(retning - 1) % 4] == '1':
        ny_retning = (retning - 1) % 4
    elif rute[retning] == '1':
        ny_retning = retning
    elif rute[(retning + 1) % 4] == '1':
        ny_retning = (retning + 1) % 4
    elif rute[(retning + 2) % 4] == '1':
        ny_retning = (retning + 2) % 4

    if ny_retning == 0:
        return [-1, 0, ny_retning]
    if ny_retning == 1:
        return [0, 1, ny_retning]
    if ny_retning == 2:
        return [1, 0, ny_retning]
    if ny_retning == 3:
        return [0, -1, ny_retning]


fil = re.sub('[(),]', '', open('maze.txt').read()).splitlines()
størrelse = len(fil)

brett = np.array([x[i:i+4] for x in fil for i in range(0, len(x), 4)])
brett = brett.reshape((størrelse, størrelse))

testbrett = np.zeros((størrelse, størrelse))

retning = 2
y = 0
x = 0

steg = 0
while x != størrelse-1 or y != størrelse-1:
    ny_y, ny_x, retning = gå_retning(brett[y, x], retning)

    y += ny_y
    x += ny_x

    steg += 1

print(steg)
