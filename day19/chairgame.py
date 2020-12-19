from collections import Counter
import numpy as np


def rotate(list, rotation):
    rotation = rotation % len(list)

    return list[-rotation:] + list[:-rotation]


def rule1(steps, people):
    for _ in range(len(people)-1):
        people = rotate(people, steps)
        del people[0]

    return people[0]


def rule2(steps, people):
    t = 0
    for _ in range(len(people)-1):
        people = rotate(people, steps)
        del people[t]
        t = (t+1) % len(people)

    return people[0]


def rule3(steps, people):
    while len(people) > 2:
        people = rotate(people, steps)

        mIndex = int(len(people)/2)
        mIndex = [mIndex, mIndex - 1] if len(people) % 2 == 0 else mIndex

        people = np.delete(people, mIndex).tolist()

    people = rotate(people, steps)

    return people[1]


def rule4(steps, people):
    for _ in range(len(people)-1):
        people = rotate(people, steps)
        people = people[:-1]

    return people[0]


rules = {'1': rule1, '2': rule2, '3': rule3, '4': rule4}

counter = Counter()

for line in open('input.txt').read().splitlines():
    rule, step, people = line.split(' ', 2)
    counter[rules[rule](int(step), people[1:-1].split(', '))] += 1

print(f'Best elf: {counter.most_common(1)[0][0]}')
