import numpy as np
from aocd import get_data

inp = get_data(day=2, year=2021)
lines = inp.splitlines()
#numbers = [int(line) for line in lines]
#arrayinp = np.asarray(numbers)

#print(numbers)

## Part A
depth = 0
horizontal = 0
for item in lines:
    match item.split():
        case ['forward', num]:
            horizontal += int(num)
        case ['down', num]:
            depth += int(num)
        case ['up', num]:
            depth -= int(num)
        case _:
            raise Exception("not known")

print(f"Depth {depth}")
print(f"horizontal {horizontal}")
print(f"Result {depth*horizontal}")
