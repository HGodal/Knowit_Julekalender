with open('forest.txt') as f:
    rows = [list(line)[:-1] for line in f]
    cols = [list(col) for col in zip(*rows)]

trees = [[]]

for col in cols:
    if col.count('#') == 0:
        trees.append([])
    else:
        trees[-1].append(''.join(col))


all_trees = list(filter(None, trees))  # Removes empty columns

symTrees = sum([tree[::1] == tree[::-1] for tree in all_trees])

print(f'Number of symmetrical trees: {symTrees}')
