import numpy as np
from aocd import get_data

inp = get_data(day=10, year=2021)
lines = inp.splitlines()
#numbers = [int(line) for line in lines]
#arrayinp = np.asarray(numbers)

#print(numbers)

print("---Part A---")

closers = {")": "(", "]": "[", "}": "{", ">": "<"}
a_closer_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
b_closer_score = {")": 1, "]": 2, "}": 3, ">": 4}


def find_pairs(line):
    for i, char in enumerate(line):
        if char in closers.keys():
            if i == 0 or line[i - 1] != closers[char]:
                raise ValueError("no opener found")
            del line[i]
            del line[i - 1]
            return line
    raise ValueError("no closers left")


score = 0
incomplete = []
for orig_line in lines:
    line = list(orig_line)
    while True:
        try:
            line = find_pairs(line)
        except ValueError:
            break
    continue_further = False
    for char in line:
        if char in closers.keys():
            score += a_closer_score[char]
            continue_further = True
            break
    if continue_further:
        continue
    incomplete.append(line)

print(score)


print("---Part B---")
scores = []
for line in incomplete:
    missing = reversed(line)
    score = 0
    for i, char in enumerate(missing):
        missing_bracket = list(closers.keys())[list(closers.values()).index(char)]
        score = score * 5
        score += b_closer_score[missing_bracket]
    scores.append(score)
scores = sorted(scores)
print(scores[int((len(scores) - 1) / 2)])

print("end")
