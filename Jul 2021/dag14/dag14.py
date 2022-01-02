from collections import defaultdict
from itertools import permutations as pms


def all_pairs(lst):
    for p in pms(lst):
        i = iter(p)
        yield tuple(zip(i, i))


def is_troll(inds):
    if not len(inds) == 4:
        return False

    if len(inds[3]) < 2:
        return False

    for t in inds[0]:
        for r in inds[1]:
            for o in inds[2]:
                for ll in all_pairs(inds[3]):
                    valid = True
                    combo = [t, r, o, ll[0][0], ll[0][1]]
                    for i in range(len(combo)-1):
                        diff = combo[i+1] - combo[i]
                        if diff <= 1 or diff > 6:
                            valid = False
                    if valid:
                        return True
    return False


def is_nisse(inds, word):
    if word[0] == 'n' or word[-1] == 'e':
        return False

    if not len(inds) == 4:
        return False

    if len(inds[2]) < 2:
        return False

    for n in inds[0]:
        for i_ in inds[1]:
            for ss in all_pairs(inds[2]):
                for e in inds[3]:
                    valid = True
                    combo = [n, i_, ss[0][0], ss[0][1], e]
                    for i in range(len(combo)-1):
                        diff = combo[i+1] - combo[i]
                        if diff <= 0 or diff > 3:
                            valid = False
                    if valid:
                        return True
    return False


words = open('ordliste.txt').read().splitlines()

troll_order = ['t', 'r', 'o', 'l']
nisse_order = ['n', 'i', 's', 'e']

counter = 0

for word in words:
    troll = defaultdict(list)
    nisse = defaultdict(list)

    for i, letter in enumerate(word):
        if letter in set('troll'):
            troll[letter].append(i)
        if letter in set('nisse'):
            nisse[letter].append(i)

    s_troll = list({k: troll[k] for k in troll_order if k in troll}.values())
    s_nisse = list({k: nisse[k] for k in nisse_order if k in nisse}.values())

    if is_troll(s_troll):
        counter += 1

    if is_nisse(s_nisse, word):
        counter += 1

print(counter)
