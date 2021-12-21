import numpy as np
from aocd import get_data

inp = get_data(day=13, year=2021)

inpdots, folds = inp.split("\n\n")
folds = [line.removeprefix("fold along ") for line in folds.splitlines()]
inpdots = [line.split(",") for line in inpdots.splitlines()]
inpdots = np.asarray(inpdots).astype(int)

dots = np.zeros(np.max(inpdots, axis=0) + 1).astype(bool)
for dot in inpdots:
    dots[dot[0], dot[1]] = True
dots = np.transpose(dots)


print("---Part A---")

for fold in folds:
    axis = 0 if fold.startswith("y") else 1
    ind = fold.split("=")[1]
    part1, part2 = np.split(dots, [int(ind)], axis=axis)
    part2 = np.delete(part2, 0, axis=axis)
    dots = part1 | np.flip(part2, axis=axis)
    print(dots.sum())


print("---Part B---")

for line in dots:
    for char in line:
        if char:
            print("#", end='')
        else:
            print(".", end='')
        print(" ", end="")
    print("")

print("end")
