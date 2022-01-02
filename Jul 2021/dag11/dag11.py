from collections import Counter
from tqdm import tqdm


oversikt = dict()
oversikt2 = dict()
kryptert = open('locked.txt').read().splitlines()
alle_navn = open('names.txt').read().splitlines()

for navn in tqdm(alle_navn):
    navneliste = [navn]
    for i in range(len(navn)-1):
        flip = navn[i:i+2][::-1]
        navneliste.append(navn[:i] + flip + navn[i+2:])

    for krypto in kryptert:
        for navnmiks in navneliste:
            j = 0
            overfladisk = 0
            for i in range(len(krypto)):
                if krypto[i] == navnmiks[j]:
                    j += 1
                elif j > 0:
                    overfladisk += 1

                if j == len(navnmiks):
                    if krypto in oversikt:
                        if oversikt[krypto][1] > overfladisk:
                            oversikt[krypto] = [navneliste[0], overfladisk]
                            oversikt2[krypto] = navneliste[0]
                        elif oversikt[krypto][1] == overfladisk and not oversikt[krypto][0] == navneliste[0]:
                            oversikt[krypto] = [None, overfladisk]
                            oversikt2[krypto] = None
                    else:
                        oversikt[krypto] = [navneliste[0], overfladisk]
                        oversikt2[krypto] = navneliste[0]
                    break

print(Counter(oversikt2.values()).most_common(2)[1])
