from collections import defaultdict

data = [line[:-1].split(',')[::-1] for line in open('leker.txt')]

scores = defaultdict(int)

for event in data:
    for i, contestant in enumerate(event):
        scores[contestant] += i

best_elf = max(scores, key=scores.get)

print(f'Best elf: {best_elf}-{scores[best_elf]}')
