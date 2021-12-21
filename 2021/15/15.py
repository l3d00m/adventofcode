import numpy as np
from aocd import get_data
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

inp = get_data(day=15, year=2021)
lines = inp.splitlines()
numbers = [list(line) for line in lines]
arrayinp = np.asarray(numbers).astype(int)

#print(numbers)

print("---Part A---")

grid = Grid(matrix=arrayinp)
path, runs = AStarFinder().find_path(grid.node(0, 0), grid.node(-1, -1), grid)
print(grid.grid_str(path=path))

sum = 0
for itm in path:
    if itm == (0, 0):
        continue
    sum += arrayinp[itm[1], itm[0]]
print(sum)

print("---Part B---")


print("end")
