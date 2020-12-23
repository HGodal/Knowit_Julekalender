from collections import Counter

counter = Counter()

for i, line in enumerate(open('input.txt').readlines()):
    text, names = line.split(' ', 1)
    names = [x.lower() for x in names[1:-2].split(', ')]
    for name in names:
        j = 0
        tempstr = ''
        newstring = ''
        for letter in text:
            if j < len(name) and letter == name[j]:
                tempstr += letter
                j += 1
            else:
                newstring += letter
        if tempstr == name:
            counter[i] += 1
            text = newstring

print(f'Line with most names: {counter.most_common(1)[0][0]}')
