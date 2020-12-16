words = {word for word in open('wordlist.txt').read().splitlines()}
riddles = {word for word in open('riddles.txt').read().splitlines()}

glue = set()

for par in riddles:
    start, end = par.split(', ')
    part1 = {word[len(start):] for word in words if word.startswith(start)}
    part2 = {word for word in part1 if word in words and word + end in words}
    glue.update(part2)

print(f'Number of chars in glue-words: {sum([len(word) for word in glue])}')
