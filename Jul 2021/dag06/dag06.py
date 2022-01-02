from math import ceil, floor
from tqdm import tqdm

pakker = [x.split(',') for x in open('pakker.txt').read().splitlines()]
pakker = [[int(x) for x in pakke] for pakke in pakker]

overste_rad = [0]*20
pakker_falt_av = 0

for indeks, lengde in tqdm(pakker):
    venstre = overste_rad[indeks: indeks+ceil((lengde)/2)]
    høyre = overste_rad[indeks+floor((lengde)/2): indeks+lengde]

    if max(venstre) == max(høyre):
        overste_rad[indeks: indeks+lengde] = [max(venstre)+1]*lengde

    else:
        pakker_falt_av += 1

print(pakker_falt_av)
