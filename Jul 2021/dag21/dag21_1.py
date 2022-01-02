# melding = 45205145192051057281419115181357209121021125181201516161911252091475141221011351923522729182181222718192919149121210211251491919514

melding = 7154102112
melding = [int(x) for x in str(melding)]

alfabet = list(' abcdefghijklmnopqrstuvwxyzæøå')
ordliste = open('wordlist.txt').read().splitlines()


def valider(tekstbit, ordliste=ordliste):
    lengde = len(tekstbit)
    for tekst in ordliste:
        if tekstbit == tekst[:lengde]:
            return True

    return False


i = 0
kombinasjoner = ['']
while i < len(melding):
    tall_lite = melding[i]
    tall_stort = int(''.join([str(x) for x in melding[i:i+2]]))

    b1 = alfabet[tall_lite]
    b2 = alfabet[tall_stort] if tall_stort <= 29 else '1'

    kombostørrelse = len(kombinasjoner)
    k1 = False
    k2 = False
    j = 0
    while j < kombostørrelse:
        kombo = kombinasjoner[j]

        if valider(kombo + b1):
            print('true1')
            k1 = True
            kombinasjoner.append(kombo + b1)

        if valider(kombo + b2):
            print('true2')
            k2 = True
            kombinasjoner.append(kombo + b2)

        j += 1

    print(kombinasjoner)

    if k1 and not k2:
        pass
    else:
        kombinasjoner = kombinasjoner[kombostørrelse:]
    print(kombinasjoner)

    i += 1
