overs = [1854803357, 2787141611, 1159251923]
snill = [2424154637, 2807727397, 2537380333]

år = [set(), set(), set()]

for antall in range(2000):
    for j in range(3):
        år[j].add(snill[j]*antall+overs[j])

print(set.intersection(*år))
