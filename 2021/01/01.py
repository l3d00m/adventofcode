import numpy as np
from aocd import get_data

inp = get_data(day=1, year=2021)
lines = inp.splitlines()
numbers = [int(line) for line in lines]
arrayinp = np.asarray(numbers)

#print(numbers)


## Part A
def count_val_increase(numbers):
    prev_item = numbers[0]
    count = 0
    for item in numbers:
        if item > prev_item:
            count += 1
        prev_item = item
    return count


print(count_val_increase(numbers))

## Part A with np
shiftedarray = np.roll(arrayinp, 1)
shiftedarray[0] = arrayinp[1]
shiftedarray[-1] = arrayinp[-1]

print((arrayinp > shiftedarray).sum())


## Part B
averages = np.convolve(numbers, np.ones(3, dtype=int), 'valid')
print(count_val_increase(averages))
