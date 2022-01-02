enkle_tall = {'en': 1, 'to': 2, 'tre': 3, 'fire': 4,
              'fem': 5, 'seks': 6, 'sju': 7, 'åtte': 8, 'ni': 9}
doble_tall = {'ti': 10, 'tjue': 20, 'tretti': 30, 'førti': 40, 'femti': 50}
tiere_tall = {'elleve': 11, 'tolv': 12, 'tretten': 13, 'fjorten': 14,
              'femten': 15, 'seksten': 16, 'sytten': 17, 'atten': 18, 'nitten': 19}
alle_tall = {**enkle_tall, **doble_tall, **tiere_tall}

text = open('tall.txt').read()
ekte_tall = [0]

tekst_tall = ['']

i = 0
while i < len(text)-1:
    for j in range(i+11, 0, -1):
        subtext = text[i:j]
        if subtext in alle_tall:
            if ekte_tall[-1] % 10 == 0 and subtext in enkle_tall and ekte_tall[-1] < 50 and ekte_tall[-1] > 10:
                ekte_tall[-1] += alle_tall[subtext]
                tekst_tall[-1] += subtext
            else:
                ekte_tall.append(alle_tall[subtext])
                tekst_tall.append(subtext)
            i = j
            break

print(sum(ekte_tall[1:]))

textfile = open('tmp.txt', 'w')
for teksttall in tekst_tall:
    textfile.write(teksttall + '\n')

# print(tekst_tall)
