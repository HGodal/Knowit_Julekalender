
usortert = open('alverekke.txt').read()
usortert = usortert.replace('Æ', chr(93)).replace(
    'Ø', chr(94)).replace('Å', chr(95))
usortert = usortert.replace('æ', chr(123)).replace(
    'ø', chr(124)).replace('å', chr(125))

usortert = usortert.splitlines()
sortert = sorted(usortert)


i = 0
while i < len(usortert):
    navn1 = usortert[i]
    navn2 = sortert[i]

    if navn1 == navn2:
        i += 1
    else:
        usortert.remove(navn2)
        sortert.remove(navn2)


print(sum([len(x) for x in usortert]))
