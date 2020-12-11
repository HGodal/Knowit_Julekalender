def calculate_time(current, locations, times):
    for place, coordinate in locations.items():
        distance = abs(coordinate[0] - current[0]) + \
            abs(coordinate[1] - current[1])

        if distance == 0:
            times[place] += 0
        elif distance < 5:
            times[place] += 0.25
        elif distance < 20:
            times[place] += 0.5
        elif distance < 50:
            times[place] += 0.75
        else:
            times[place] += 1


def move_to_place(current, upcoming):
    xChange = 1 if current[0] < upcoming[0] else -1
    for xCoor in range(current[0] + xChange, upcoming[0] + xChange, xChange):
        current = (xCoor, current[1])
        calculate_time(current, locations, times)

    yChange = 1 if current[1] < upcoming[1] else -1
    for yCoor in range(current[1] + yChange, upcoming[1] + yChange, yChange):
        current = (current[0], yCoor)
        calculate_time(current, locations, times)

    return current


info = open('input.txt').read().splitlines()
places, route = [info[:50], info[50::]]

locations = {}
for place in places:
    place = place.split(':')
    locations[place[0]] = eval(place[1])

times = dict.fromkeys(locations, 0)

current = (0, 0)
for place in route:
    current = move_to_place(current, locations[place])

difference = max(times.values()) - min(times.values())
print(f'Largest time differende: {difference}')
