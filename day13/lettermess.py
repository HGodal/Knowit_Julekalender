from collections import Counter

lettercount = Counter()
wordlist = ''

for char in open('text.txt').read()[:-1]:
    wordlist += char if lettercount[char] == ord(char) - 97 else ''
    lettercount[char] += 1
print(f'Answer: {wordlist}')
