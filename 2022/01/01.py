import numpy as np
from aocd import get_data

inp = get_data(day=1, year=2022)
#inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
elves = [[int(cal) for cal in elf.splitlines()] for elf in inp.split("\n\n")]

sums = []
for elve in elves:
    sums.append(sum(elve))
sums = list(reversed(sorted(sums)))
print(sums[0])
print(sum(sums[0:3]))

