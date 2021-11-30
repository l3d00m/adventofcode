from pathlib import Path
from aocd import get_data
lines = get_data(day=24, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

directions = []

for line in lines:
    line_directions = []
    while len(line) > 0:
        if line.startswith(("e", "w")):
            line_directions.append(line[0])
            line = line[1:]
        else:
            line_directions.append(line[0:2])
            line = line[2:]
    directions.append(line_directions)


def move(direction):
    x = 0
    y = 0
    for mv in direction:
        if mv == "w":
            x -= 1
        elif mv == "e":
            x += 1
        elif mv == "ne":
            y += 1
            x += 1
        elif mv == "sw":
            y -= 1
            x -= 1
        elif mv == "se":
            y -= 1
        elif mv == "nw":
            y += 1
    return x, y


#print(move(["ne", "se", "w"]))
#print(move(["nw", "sw", "e"]))
flipped_tiles = []
for direction in directions:
    el = move(direction)
    if el in flipped_tiles:
        flipped_tiles.remove(el)
    else:
        flipped_tiles.append(el)
print(len(flipped_tiles))


## PART B
flipped_tiles = set(flipped_tiles)
for i in range(100):
    xs = [el[0] for el in flipped_tiles]
    ys = [el[1] for el in flipped_tiles]
    new_flipped_tiles = flipped_tiles.copy()
    for x in range(min(xs) - 2, max(xs) + 2):
        for y in range(min(ys) - 2, max(ys) + 2):
            this_el = (x, y)
            adjs = set([(x - 1, y), (x + 1, y), (x + 1, y + 1), (x - 1, y - 1), (x, y - 1), (x, y + 1)])
            cnt = len(flipped_tiles & adjs)
            if cnt == 2 and this_el not in flipped_tiles:
                new_flipped_tiles.add(this_el)
            elif (cnt == 0 or cnt > 2) and this_el in flipped_tiles:
                new_flipped_tiles.remove(this_el)
    flipped_tiles = set(new_flipped_tiles)

print(len(flipped_tiles))
