import numpy as np
from aocd import get_data

inp = get_data(day=4, year=2021)

#numbers = [int(line) for line in lines]
#arrayinp = np.asarray(numbers)

#print(numbers)

print("---Part A---")
blocks = inp.split("\n\n")
winners = [int(itm) for itm in blocks.pop(0).split(",")]
bingos = []
for block in blocks:
    bingo = []
    for row in block.splitlines():
        bingo.append([int(itm) for itm in row.split()])
    bingos.append(bingo)
bingos = np.array(bingos)


def play(bingos, winners):
    drawn = []
    for winner in winners:
        drawn.append(winner)
        for bingo_index, bingo in enumerate(bingos):
            for row in bingo:
                if np.isin(row, drawn).all():
                    return bingo, drawn
            for col in np.transpose(bingo):
                if np.isin(col, drawn).all():
                    return bingo, drawn


bingo, drawn = play(bingos, winners)


def calc_final(bingo, drawn):
    last = drawn[-1]
    endsum = 0
    for row in bingo:
        for item in row:
            if item not in drawn:
                endsum += item
    return last * endsum


print(f"Result1 {calc_final(bingo, drawn)}")

print("---Part B---")


def play2(bingos, winners):
    drawn = []
    boards_won = []
    for winner in winners:
        drawn.append(winner)
        for bingo_index, bingo in enumerate(bingos):
            for row in bingo:
                if np.isin(row, drawn).all():
                    if bingo_index not in boards_won:
                        boards_won.append(bingo_index)
                        if (len(boards_won) == len(bingos)):
                            return bingo, drawn
            for col in np.transpose(bingo):
                if np.isin(col, drawn).all():
                    if bingo_index not in boards_won:
                        boards_won.append(bingo_index)
                        if (len(boards_won) == len(bingos)):
                            return bingo, drawn


bingo, drawn = play2(bingos, winners)
print(f"Result2 {calc_final(bingo, drawn)}")
