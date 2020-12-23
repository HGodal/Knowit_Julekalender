from collections import defaultdict


def find_santa(dictionary, counter):
    for i in range(1, 6):
        for person in dictionary[i]:
            if person == 'Claus':
                return counter
            else:
                counter += 1
    return counter


people = defaultdict(list)
counter = 0

for line in open('input.txt').read().splitlines():
    if line == '---':
        counter += 1
        for i in range(1, 6):
            if people[i]:
                people[i].pop(0)
                break
    else:
        name, priority = line.split(',')
        people[int(priority)].append(name)

print(f'Elves before Claus: {find_santa(people, counter)}')
