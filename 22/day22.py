from pathlib import Path
from aocd import get_data
lines = get_data(day=22, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

lines = [line for line in lines if not line.startswith("Player")]

# Split lines by empty element into parts
from itertools import groupby
player1, player2 = [list(g) for k, g in groupby(lines, key=bool) if k]
player1 = [int(num) for num in player1]
player2 = [int(num) for num in player2]

while len(player1) >= 1 and len(player2) >= 1:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)
winner = player1 if len(player1) > 1 else player2
import numpy as np
weighted = np.multiply(np.array(list(reversed(winner))), np.arange(1, len(winner) + 1))
print(sum(weighted))

