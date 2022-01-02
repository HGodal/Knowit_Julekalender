
oversikt = open('task.txt').read().splitlines()
oversikt = [x.split(' ')[0] for x in oversikt]

forrige = oversikt[0]

i = 1
vare = False
while i < len(oversikt):
    gjeldende = oversikt[i]

    if len(forrige) >= len(gjeldende) and 'K' in forrige:
        del oversikt[i-1]
        forrige = oversikt[i-2]
        i -= 1
    else:
        forrige = gjeldende
        i += 1

print(''.join(oversikt).count('K'))
