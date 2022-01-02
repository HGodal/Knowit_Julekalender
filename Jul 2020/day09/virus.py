import numpy as np

sick_elves = np.array([list(line) for line in open('elves.txt')]) == 'S'

num_sick_elves = [sick_elves.sum()]

while True:
    extended_sick_elves = np.pad(sick_elves.astype(int), 1)
    left = extended_sick_elves[:-2, 1:-1]
    right = extended_sick_elves[2:, 1:-1]
    over = extended_sick_elves[1:-1, :-2]
    under = extended_sick_elves[1:-1, 2:]

    sick_elves += np.array(left + right + over + under) >= 2

    if sick_elves.sum() == num_sick_elves[-1]:
        break

    num_sick_elves.append(sick_elves.sum())

print(f'Dager før viruset stopper: {len(num_sick_elves)}')
