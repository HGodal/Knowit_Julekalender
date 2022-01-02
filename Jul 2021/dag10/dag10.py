from itertools import permutations as pms


alle_muligheter = pms([1, 2, 3, 4, 5, 6, 7, 8, 9])
starter_på_d = [x for x in alle_muligheter if x[0] == 4]
åtte_tegn = [x[:-1] for x in starter_på_d]
åtte_tegn = list(set(tuple(sub) for sub in åtte_tegn))

antall = 0

for kombinasjon in åtte_tegn:
    virker = True

    for i in range(len(kombinasjon)-1):
        tall = kombinasjon[i]
        neste_tall = kombinasjon[i+1]
        if tall in {1, 3}:
            if neste_tall in {1, 3}:
                if not 2 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {1, 7}:
            if neste_tall in {1, 7}:
                if not 4 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {3, 9}:
            if neste_tall in {3, 9}:
                if not 6 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {7, 9}:
            if neste_tall in {7, 9}:
                if not 8 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {1, 9}:
            if neste_tall in {1, 9}:
                if not 5 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {3, 7}:
            if neste_tall in {3, 7}:
                if not 5 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {4, 6}:
            if neste_tall in {4, 6}:
                if not 5 in kombinasjon[:i]:
                    virker = False
                    break

        if tall in {2, 8}:
            if neste_tall in {2, 8}:
                if not 5 in kombinasjon[:i]:
                    virker = False
                    break

    if virker:
        antall += 1

print(antall)
