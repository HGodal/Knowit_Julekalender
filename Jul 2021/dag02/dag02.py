from math import radians, sin, cos, acos


def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    return 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


a = open('cities.csv').readlines()
b = [x.split('Point(')[1][:-2].split(' ') for x in a[1:]]
coords = [list(map(float, lst)) for lst in b]

location = [0, 90]
travel_distance = 0

while len(coords) > 0:
    dist = []
    for coord in coords:
        dist.append(great_circle(location[0], location[1], coord[0], coord[1]))

    travel_distance += min(dist)
    location = coords.pop(dist.index(min(dist)))

print(travel_distance)

travel_distance += great_circle(location[0], location[1], 0, 90)

print(travel_distance)
