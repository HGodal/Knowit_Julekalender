n_steg = 100000000000000000079//45
kolonne = n_steg*30+-5
rad = n_steg*15
nord = True

while kolonne+rad < 100000000000000000079:
    if nord:
        rad += 1
        if rad % 3 == 0 and rad % 5 != 0:
            nord = False
    else:
        kolonne += 1
        if kolonne % 5 == 0 and kolonne % 3 != 0:
            nord = True

print(f'{kolonne},{rad}')
