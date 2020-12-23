from aocd import get_data
inp = get_data(day=23, year=2020)

inp = "389125467"
in_cups = [int(char) for char in inp]
cups = in_cups.copy()


def find_dest(current, sublist):
    while current > 0:
        try:
            return sublist.index(current) + 5
        except ValueError:
            current -= 1
    return sublist.index(max(sublist)) + 5


def move(cups):
    cups = list(cups)
    dest = find_dest(cups[0], cups[4:])
    cups[dest:dest] = cups[1:4]
    del cups[1:4]
    return collections.deque(cups)


import collections
cups = collections.deque(cups)
for _ in range(100):
    cups = move(cups)
    cups.rotate(-1)

while cups[0] != 1:
    cups.rotate(1)
cups.popleft()
print(''.join([str(cup) for cup in cups]))


## PART B

def move_with_deque(cups):
    """Still much too slow, bruteforcing is probably not the solution"""
    move_els = []
    current = cups.popleft()
    for i in range(3):
        move_els.append(cups.popleft())
    to_find = current
    dest = None
    while dest is None:
        try:
            dest = cups.index(to_find) + 1
        except ValueError:
            to_find -= 1
            if to_find < 0:
                dest = cups.index(max(cups)) + 1
                break
    for el in reversed(move_els):
        cups.insert(dest, el)
    cups.insert(0, current)
    return cups


import numpy as np
cups = in_cups.copy()
cups += np.arange(max(cups) + 1, 1e6 + 1, dtype=int).tolist()

#cups = in_cups + np.arange(max(in_cups) + 1, 25 + 1, dtype=int).tolist()
#cups.rotate(-len(in_cups))

cups = collections.deque(cups)
for i in range(int(10e6)):
    #cups.rotate(i*4)
    #print(f"{i:02d}: " + ' | '.join([f"{cup:02d}" for cup in cups]))
    #cups.rotate(-i*4)
    cups = move_with_deque(cups)
    cups.rotate(-1)
