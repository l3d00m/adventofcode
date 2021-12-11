import numpy as np
from aocd import get_data

inp = get_data(day=11, year=2021)
lines = inp.splitlines()
lines = [list(line) for line in lines]
orig_inp = np.asarray(lines).astype(int)

#print(numbers)

print("---Part A---")
arrayinp = np.pad(orig_inp, 1, 'constant', constant_values=-1e6)


def iterateFlashes(inp):
    for row, line in enumerate(inp):
        for col, num in enumerate(line):
            if num > 9 and num < 1e6:
                inp[(row - 1):(row + 2), (col - 1):(col + 2)] += 1
                inp[row, col] = 1e6
                return inp, True
    return inp, False


counter = 0
for i in range(100):
    arrayinp = arrayinp + 1
    result = True
    while result:
        arrayinp, result = iterateFlashes(arrayinp)
    counter += (arrayinp >= 1e6).sum()
    arrayinp[arrayinp >= 1e6] = 0

print(counter)

print("---Part B---")
arrayinp = np.pad(orig_inp, 1, 'constant', constant_values=-1e6)
i = 0
while True:
    i += 1
    arrayinp = arrayinp + 1
    result = True
    while result:
        arrayinp, result = iterateFlashes(arrayinp)
    arrayinp[arrayinp >= 1e6] = 0
    if (np.max(arrayinp[1:-1, 1:-1]) == 0):
        break

print(i)

print("end")
