import numpy as np
from tqdm import tqdm

data = open('input.txt').read().splitlines()

bytte = 200
byer = [x.replace('(', '').replace(')', '').split(',') for x in data[:bytte]]
byer = [[int(x) for x in by] for by in byer]
rekkefølge = [int(by) for by in data[bytte:]]

kart = np.zeros((1000, 1000))

forrige_by = byer[rekkefølge[0]]

for neste_indeks in tqdm(rekkefølge[1:]):
    neste_by = byer[neste_indeks]
    x, y = list(zip(forrige_by, neste_by))
    if x[1] < x[0]:
        x = [idx+1 for idx in x]
    if y[1] < y[0]:
        y = [idx+1 for idx in y]

    kart[min(y):max(y), min(x):max(x)] += 1
    forrige_by = neste_by


x1, y1 = np.unravel_index(np.argmax(kart), kart.shape)
x2, y2 = np.array(
    kart.shape) - np.unravel_index(np.argmax(kart[::-1, ::-1]), kart.shape) - (1, 1)

print(f'{x1},{y1} {x2},{y2}')
