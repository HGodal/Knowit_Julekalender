from tqdm import tqdm

fil = open('input.txt').read()
result = dict()

for i in tqdm(range(len(fil))):
    for j in range(len(fil), i, -1):
        subset = fil[i:j]
        count_n = subset.count('N')
        count_j = subset.count('J')
        if count_n == count_j:
            result[i] = count_n*2
            break

print(dict(sorted(result.items(), key=lambda item: item[1])))
