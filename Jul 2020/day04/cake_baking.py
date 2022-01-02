from collections import defaultdict

resources = defaultdict(int)

with open("leveringsliste.txt") as f:
    for line in f:
        sanitized_line = line.replace(" ", "").split(",")
        for pair in sanitized_line:
            (key, val) = pair.split(":")
            resources[key] += int(val)

ingredients = {"sukker": 2, "mel": 3, "melk": 3, "egg": 1}
potential_cakes = []

for i in resources:
    potential_cakes.append(resources[i] // ingredients[i])

print(f"Number of cakes: {min(potential_cakes)}")
