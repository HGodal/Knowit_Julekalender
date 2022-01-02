from collections import Counter
import re


def tider(start, prodtider, pakketider):
    minutt = []
    tid = int(start[:-2]) * 60 + int(start[2:])

    for i in range(len(prodtider)):
        tid += prodtider[i]
        minutt.extend(range(tid, tid+pakketider[i]))

    return minutt


teller = Counter()
fil = open('factory.txt').read().splitlines()

for maskin in fil:
    info = re.sub('[^0-9 ]', '', maskin).split()
    start = info.pop(0)
    prod_tid = [int(x) for x in info[0::2]]
    pakke_tid = [int(x) for x in info[1::2]]

    for tid in tider(start, prod_tid, pakke_tid):
        teller[tid] += 1

print(max(teller.values()))
