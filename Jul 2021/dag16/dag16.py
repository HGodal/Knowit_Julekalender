import re


def behandle_data(sti):
    rådata = open(sti).read()
    rådata = re.sub(r'[a-z]', 'x', rådata)
    priser = list(zip(*rådata.splitlines()[::-1]))
    priser = [pris.index('x') for pris in priser]

    for i in range(0, len(priser), 24):
        yield priser[i:i + 24]


def strategi_1(forrige, neste):
    sum_priser = [sum(a) for a in zip(*forrige)]
    min_indeks = sum_priser.index(min(sum_priser))
    return sum([pris[min_indeks] for pris in neste])


def strategi_2(forrige, neste):
    sum_priser = [sum(a) for a in zip(*forrige)]
    min_indeks = sum_priser.index(min(sum_priser))

    pris = 0
    i = 0
    while i < len(neste):
        prev = forrige[i][min_indeks]
        prev_ = forrige[i+1][min_indeks]

        pris1 = 0
        pris2 = 0

        if prev < prev_:
            pris1 = neste[i][min_indeks]
            pris2 = neste[i][min_indeks+1]
            i += 1
        else:
            pris1 = neste[i][min_indeks]

        pris += (pris1 + pris2)
        i += 1

    return pris


forrige_år = list(behandle_data('strømpriser.txt'))
neste_år = list(behandle_data('strømpriser_next.txt'))

priser = [strategi_1(forrige_år, neste_år), strategi_2(forrige_år, neste_år)]
print(f'{priser.index(min(priser))+1},{max(priser)-min(priser)}')
