from collections import Counter

counter = Counter()
generation = 0
spaces = 0

previous = '('
for char in open('family.txt').read():
    if char in {'(', ')'}:
        generationchange = 1 if char == '(' else -1
        change = 0 if char == previous else generationchange

        counter[generation] += spaces - change
        generation += generationchange

        previous = char
        spaces = 0

    elif char == ' ':
        spaces += 1

print(f'Most elves in a generation: {counter.most_common(1)[0][1]}')
