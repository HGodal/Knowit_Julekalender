alfabet = 'abcdefghijklmnopqrstuvwxyzæøå'

tekster = ['wawwgjlmwkafeosjoæiralop',
           'jagwfjsuokosjpzæynzxtxfnbæjkæalektfamxæø',
           'wawwgjlmwkoåeosaæeoltååøbupscpfzqehkgdhkjdoqqkuuakvwogjkpøjsbmpq',
           'vttyøyønøbjåiåzpejsimøldajjecnbplåkyrsliænhbgkvbecvdscxømrvåmagdioftvivwøkvbnyøå']

nøkkel = 'alvalv'
keylen = len(nøkkel)
nøkkel = nøkkel + 'x' * (8 - len(nøkkel))

for tekst in tekster:
    dekryptert = ''

    blokker = [tekst[i:i+8] for i in range(0, len(tekst), 8)]
    for n, blokk in enumerate(blokker):
        for i, bokstav in enumerate(blokk):
            indeks = alfabet.index(bokstav) - i - keylen * \
                (n+1) - 2 - alfabet.index(nøkkel[i])
            dekryptert += alfabet[indeks % 29]

    print(dekryptert)
