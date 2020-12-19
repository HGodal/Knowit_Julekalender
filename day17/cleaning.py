import numpy as np


def robot_fits(area, robot):
    areaflat = area.ravel()
    robotflat = robot.ravel()

    for i in range(len(areaflat)):
        if robotflat[i] == 's' and areaflat[i] == 'x':
            return False
    return True


def clean_area(area, cleaners):
    shape = area.shape
    areaflat = area.ravel()
    cleanersflat = cleaners.ravel()

    for i in range(len(cleanersflat)):
        if cleanersflat[i] == 'k' and areaflat[i] == ' ':
            areaflat[i] = '.'

    return areaflat.reshape(shape)


robot = np.array([
    list('  sss  '),
    list(' sssss '),
    list('sssssss'),
    list('sssssss'),
    list('sssssss'),
    list(' sssss '),
    list('  sss  ')])

cleaners = np.array([
    list('kkk   kkk'),
    list('kkkkkkkkk'),
    list('kkkkkkkkk'),
    list(' kkkkkkk '),
    list(' kkkkkkk '),
    list(' kkkkkkk '),
    list('kkkkkkkkk'),
    list('kkkkkkkkk'),
    list('kkk   kkk')])

floor = np.array([list(line)[:-1] for line in open('kart.txt').readlines()])

height = len(floor) - 6
width = len(floor[0]) - 6
for i in range(height):
    for j in range(width):
        area = floor[i:7+i, j:7+j]
        if robot_fits(area, robot):
            l = 1 if j == 0 else 0
            r = 1 if width - j == 1 else 0
            t = 1 if i == 0 else 0
            b = 1 if height - i == 1 else 0

            f_area = floor[i-1+t:7+i+1-b, j-1+l:7+j+1-r]
            c_area = cleaners[t:len(cleaners)-b, l:len(cleaners[0])-r]

            cleaned_area = clean_area(f_area, c_area)
            floor[(i-1+t):(7+i+1-b), (j-1+l):(7+j+1-r)] = cleaned_area

print(f'Areas not cleaned: {np.count_nonzero(floor == " ")}')
