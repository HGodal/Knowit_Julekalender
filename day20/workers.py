from collections import defaultdict

hierarchy = [line.split('🎄') for line in open('elves.txt').read().splitlines()]

all_elves = set()
for elflist in hierarchy:
    all_elves.add(elflist[-1])

for structure in hierarchy:
    for i in range(len(structure)-1, -1, -1):
        if structure[i] not in all_elves:
            structure.remove(structure[i])

# ------------------------------------------------------------------------ #

ranking = defaultdict(set)

for structure in hierarchy:
    ranking[structure[-1]]
    for i in range(len(structure)-1):
        ranking[structure[i]].add(structure[i+1])

workers = set()
middle = set()

deletelist = []
for key, value in ranking.items():
    if not value:
        workers.add(key)
        deletelist.append(key)

for i in deletelist:
    del ranking[i]

for key, value in ranking.items():
    if len(value) > 1 or max(value) in workers:
        middle.add(key)

print(f'Difference between elf-types: {len(workers) - len(middle)}')
