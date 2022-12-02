import numpy as np
from aocd import get_data

inp = get_data(day=2, year=2022)
#inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

lines = [line.split(" ") for line in inp.splitlines()]
score = 0
wins = [("A", "Y"), ("B", "Z"), ("C", "X")]
draws = [("A", "X"), ("B", "Y"), ("C", "Z")]
losses = [("A", "Z"), ("B", "X"), ("C", "Y")]

def calcScore(me):
    if me == "X":
        return 1
    if me == "Y":
        return 2
    if me == "Z":
        return 3


for line in lines:
    me = line[1]
    opp = line[0]
    score += calcScore(me)
    for item in wins:
        if opp == item[0] and me == item[1]:
            score += 6
    for item in draws:
        if opp == item[0] and me == item[1]:
            score += 3

print(score)

score = 0
for line in lines:
    me = line[1]
    opp = line[0]
    if me == "X":
        for item in losses:
            if opp == item[0]:
                score += calcScore(item[1])
    if me == "Y":
        score += 3
        for item in draws:
            if opp == item[0]:
                score += calcScore(item[1])
    if me == "Z":
        score += 6
        for item in wins:
            if opp == item[0]:
                score += calcScore(item[1])


print(score)
