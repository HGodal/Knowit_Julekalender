from collections import defaultdict
from math import floor


def lag_feilregistreringer():
    feil = dict()

    feilfil = open('feilregistreringer.txt').read().splitlines()
    feilfil = [x.split(' / ') for x in feilfil]

    for linje in feilfil:
        feil[linje[0]] = [int(x) for x in linje[1:]]

    return feil


feil = lag_feilregistreringer()


ukedager = [defaultdict(int), defaultdict(int), defaultdict(
    int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)]

data = open('skritt.txt').read()
skritt_data = data.splitlines()
antall_uker = data.count('##') + 1

for linje in skritt_data:
    linje = [x.strip() for x in linje.split('/')]

    if not linje[0] == '##':
        person, yrke = linje[:2]
        alle_skritt = linje[2:]

        for i, skritt in enumerate(alle_skritt):
            if skritt.isnumeric():
                ukedager[i][person] += max(int(skritt) - feil[yrke][i], 0)
            else:
                ukedager[i][person] += 0

svar = ''
for dag in ukedager:
    nisse = dag.pop('Nissen 🎅')
    svar += str(floor(nisse/antall_uker - sum(dag.values()) /
                (antall_uker*len(dag.values()))))

print(svar)
