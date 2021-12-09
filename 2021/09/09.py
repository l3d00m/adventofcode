import numpy as np
from aocd import get_data

inp = get_data(day=9, year=2021)
lines = inp.splitlines()
numbers = [list(line) for line in lines]
arrayinp = np.asarray(numbers).astype(int)

print("---Part A---")


def calcLowest(inp):
    comparer = np.roll(inp, 1, axis=0)
    comparer[0] = 100
    result = inp < comparer
    comparer = np.roll(inp, -1, axis=0)
    comparer[-1] = 100
    result &= inp < comparer
    return result


result = calcLowest(arrayinp) & np.transpose(calcLowest(np.transpose(arrayinp)))

relevant_levels = arrayinp[result.astype(bool)] + 1
print(sum(relevant_levels))


print("---Part B---")


def check(inp, row, col, checked):
    to_check = np.zeros_like(inp).astype(bool)
    if not inp[row, col]:
        return to_check
    for i in range(row + 1, inp.shape[0]):
        if inp[i, col] == 0:
            break
        elif checked[i, col] == 0:
            to_check[i, col] = 1
    for i in range(row - 1, -1, -1):
        if inp[i, col] == 0:
            break
        elif checked[i, col] == 0:
            to_check[i, col] = 1
    for i in range(col + 1, inp.shape[1]):
        if inp[row, i] == 0:
            break
        elif checked[row, i] == 0:
            to_check[row, i] = 1
    for i in range(col - 1, -1, -1):
        if inp[row, i] == 0:
            break
        elif checked[row, i] == 0:
            to_check[row, i] = 1
    return to_check


basin_inp = np.array(arrayinp != 9).astype(int)
checked = np.zeros_like(basin_inp).astype(bool)
to_check = np.zeros_like(basin_inp).astype(bool)
result = np.zeros_like(basin_inp)
while np.min(checked) == 0:
    to_check[np.where(checked == 0)[0][0], np.where(checked == 0)[1][0]] = 1
    size_sum = 0
    while np.max(to_check) == 1:
        row = np.where(to_check == 1)[0][0]
        col = np.where(to_check == 1)[1][0]
        checked[row, col] = True
        size_sum += basin_inp[row, col]

        to_check_returned = check(basin_inp, row, col, checked)

        to_check |= to_check_returned
        to_check[row, col] = 0
    result[row, col] = size_sum

max_values = result.flatten()
biggest3 = max_values[np.argsort((max_values))[-3:]]
print(np.prod(biggest3))
print("end")
