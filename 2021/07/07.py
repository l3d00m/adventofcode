import numpy as np
from aocd import get_data
import math

inp = get_data(day=7, year=2021)
#inp = "16,1,2,0,4,2,7,1,2,14"
init_crabs = [int(itm) for itm in inp.split(",")]

print("---Part A---")

target = np.full_like(init_crabs, np.median(init_crabs))
sum = np.abs(init_crabs - target).sum()
print(sum)


print("---Part B---")
target = math.floor(np.average(init_crabs))
sum = 0
for crab in init_crabs:
    dist = np.abs(crab - target)
    sum += np.array(range(dist + 1)).sum()
print(sum)


print("end")
