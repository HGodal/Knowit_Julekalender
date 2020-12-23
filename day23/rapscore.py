from collections import defaultdict

wordscore = defaultdict(int)
score = defaultdict(int)

for line in open('basewords.txt').read().splitlines():
    word, value = line.split(' ')
    wordscore[word] = int(value)

for line in open('rap_battle.txt').read().splitlines():
    elf, rap = line.split(': ')

    previous = ''
    counter = 1
    previous_vowels = 0

    for word in rap.split(' '):
        jul = False

        baseword = word
        if word[:4] == 'jule':
            baseword = word[4:]

        vowels = sum(map(word.count, "aeiouyæøå"))
        vowelbonus = 0

        if previous != '' and vowels > previous_vowels:
            jul = True if word[:4] == 'jule' else jul
            vowelbonus = vowels - previous_vowels
        previous_vowels = vowels

        if previous == baseword:
            counter += 1
        else:
            counter = 1
            previous = baseword

        score[elf] += int((wordscore[baseword] + vowelbonus*(jul+1))/counter)

bestelf = max(score, key=score.get)
print(f'Best elf: {bestelf},{score[bestelf]}')
