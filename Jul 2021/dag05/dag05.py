tree = open('tree.txt').read().replace('Grinch)', '')
tree = ''.join([x for x in tree if x in {'(', ')'}])

depth = 0
deepest_depth = 0

for letter in tree:
    if letter == '(':
        depth += 1

    elif letter == ')':
        depth -= 1

    if deepest_depth < depth:
        deepest_depth = depth

print(deepest_depth)
