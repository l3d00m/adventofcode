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


def print_result(winner_cards):
    import numpy as np
    weighted = np.multiply(np.array(list(reversed(winner_cards))), np.arange(1, len(winner_cards) + 1))
    print(sum(weighted))


def play_round(player1, player2, partb=False):
    played_games = []
    while len(player1) >= 1 and len(player2) >= 1:
        if (player1, player2) in played_games:
            return 1, player1
        played_games.append((player1[:], player2[:]))
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if partb and card1 <= len(player1) and card2 <= len(player2):
            # Recurse only in part b
            winner, _ = play_round(player1[:card1], player2[:card2])
        else:
            winner = 1 if card1 > card2 else 2
        if winner == 1:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return (1, player1) if len(player1) >= 1 else (2, player2)


_, winner_cards = play_round(player1[:], player2[:])
print_result(winner_cards)
_, winner_cards = play_round(player1[:], player2[:], partb=True)
print_result(winner_cards)
