import numpy as np
from aocd import get_data

inp = get_data(day=3, year=2021)
lines = inp.splitlines()
chars = [list(line) for line in lines]
#arrayinp = np.asarray(numbers)

#print(numbers)

print("---Part A---")


def convertBitsToInt(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out


stuff = np.asarray(chars, dtype=int).astype(bool)

gammabits = np.sum(stuff, axis=0) > len(lines) / 2
gamma = convertBitsToInt(gammabits)
eps = convertBitsToInt(~gammabits)
print(gamma * eps)

print("---Part B---")
possible_results = stuff
pos = 0
while len(possible_results) > 1:
    keep_ones = np.count_nonzero(possible_results[:, pos] == 1) >= np.count_nonzero(possible_results[:, pos] == 0)
    possible_results = np.delete(possible_results, possible_results[:, pos] != keep_ones, axis=0)
    pos += 1

oxygen = convertBitsToInt(possible_results[0])
print(f"Oxgen {oxygen}")

possible_results = stuff
pos = 0
while len(possible_results) > 1:
    keep_ones = np.count_nonzero(possible_results[:, pos] == 1) < np.count_nonzero(possible_results[:, pos] == 0)
    possible_results = np.delete(possible_results, possible_results[:, pos] != keep_ones, axis=0)
    pos += 1

co2 = convertBitsToInt(possible_results[0])
print(f"CO2 {co2}")
print(co2 * oxygen)
