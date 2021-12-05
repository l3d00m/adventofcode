import numpy as np
from aocd import get_data

inp = get_data(day=5, year=2021)

lines = inp.splitlines()
#numbers = [int(line) for line in lines]
#arrayinp = np.asarray(numbers)

incoords = []
for line in lines:
    line = line.replace(",", " ").split()
    x1 = int(line[0])
    y1 = int(line[1])
    x2 = int(line[3])
    y2 = int(line[4])
    incoords.append([[x1, x2], [y1, y2]])

coords = []
diagonal_coords = []
for itm in incoords:
    if itm[0][0] == itm[0][1] or itm[1][0] == itm[1][1]:
        coords.append(itm)
    else:
        diagonal_coords.append(itm)
result = np.zeros((1000, 1000), dtype=int)

print("---Part A---")
for coord in coords:
    x = (coord[0][0], coord[0][1]) if coord[0][0] <= coord[0][1] else (coord[0][1], coord[0][0])
    y = (coord[1][0], coord[1][1]) if coord[1][0] <= coord[1][1] else (coord[1][1], coord[1][0])
    if (x[0] == x[1]):
        result[x[0], y[0]: (y[1] + 1)] += 1
    elif (y[0] == y[1]):
        result[x[0]: (x[1] + 1), y[1]] += 1

print(np.count_nonzero(result >= 2))


print("---Part B---")

for coord in diagonal_coords:
    xsign = (1 if coord[0][0] < coord[0][1] else -1)
    ysign = (1 if coord[1][0] < coord[1][1] else -1)
    xcoords = np.arange(coord[0][0], (coord[0][1] + xsign), xsign)
    ycoords = np.arange(coord[1][0], (coord[1][1] + ysign), ysign)
    newcoords = np.transpose(np.vstack((xcoords, ycoords)))
    for newcoord in newcoords:
        result[newcoord[0], newcoord[1]] += 1

print(np.count_nonzero(result >= 2))
print("end")
