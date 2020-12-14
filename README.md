# My solutions to Advent of Code 2020 in Python

I started off with Jupyter Notebooks and later switched to Python scripts.

# Things I learned

## Day 10

Memoization: Store the function result for the given parameters

Induction: Calculate the values in reverse order


## Day 12

- Swapping elements in a python array is easy: `waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]`

## Day 13

- `if` in list comprehensions: `[int(line) for line in line[1].split(",") if line is not "x" ]`


## Day 14

- itertools has some black magic stuff, e.g. `product` can be used to calculate all combinations from a list of tuples.