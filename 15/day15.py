import math
from pathlib import Path

puzzle_in = [1, 12, 0, 20, 8, 16]


def get_number_a(start_turns, index_spoken):
    """Stores all turns in a list and iterates the list backwards for lookup. Not very efficient."""
    turns = start_turns.copy()
    for i in range(len(turns), index_spoken):
        last_i = i - 1
        last_num = turns[last_i]
        last_spoken_index = last_i
        for i2 in range(i-2, -1, -1):
            if turns[i2] == last_num:
                last_spoken_index = i2
                break
        age = last_i - last_spoken_index
        turns.append(age)
    return age


def get_number_b(start_turns, index_spoken):
    """Stores only the last occurence for each number in a dict. 
       More efficient, but still takes longer than it normally should for an AoC puzzle."""
    numbers = {}
    for i, val in enumerate(start_turns):
        numbers[val] = i
    # Not a good assumption to make, but correct for my input...
    next_age = 0
    for i in range(len(start_turns), index_spoken):
        # Store the number from this run, which is calculated in the last run
        this_number = next_age
        # Lookup correct age for next run before storing the current one
        last_spoken_index = numbers.get(this_number, i)
        next_age = i - last_spoken_index
        # Now store the age for this turn
        numbers[this_number] = i
    return this_number


print(get_number_a(puzzle_in, 2020))
print(get_number_b(puzzle_in, 30000000))
