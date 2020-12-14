abc = 'abcdefghijklmnopqrstuvwxyz'


def alter_word(s1):
    s2 = ''.join(abc[(abc.index(char) + 1) % 26] for char in s1)[1::]
    return ''.join(abc[(abc.index(c1) + abc.index(c2)) % 26] for _, (c2, c1) in enumerate(zip(s2, s1)))


password = 'eamqia'
for word in open('hint.txt').read().splitlines():
    wordlist = []

    for i in range(len(word)):
        wordlist.append(list(word) + [''] * i)
        word = alter_word(word)

    transposed = [''.join(line).strip() for line in list(zip(*wordlist))]

    for text in transposed:
        if password in text:
            print(f"'{''.join(wordlist[0])}' is a hint for the password '{password}'")
            break
