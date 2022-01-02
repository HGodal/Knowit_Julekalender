maur = 1
tau = 20

while maur < tau:
    tau += 20
    maur += maur*(20/(tau-20)) + 1

print(f'Maur: {int(maur/100)}, Tau: {int(tau/100)}')
