from pathlib import Path
from aocd import get_data
lines = get_data(day=12, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
   lines2 = f.read().splitlines()

# lines = [line.replace("L","#") for line in lines]

# 1 east, 2 south, 3 west, 0 north
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
direction = EAST
pos = [0]*4
for line in lines:
    this_direction = direction
    val = int(line[1:])
    if line.startswith("F"):
        pass
    elif line.startswith("N"):
        this_direction = NORTH
    elif line.startswith("E"):
        this_direction = EAST
    elif line.startswith("S"):
        this_direction = SOUTH
    elif line.startswith("W"):
        this_direction = WEST
    elif line.startswith("R"):
        direction = (direction + int(val/90)) % 4
        continue
    elif line.startswith("L"):
        direction = (direction - int(val/90)) % 4
        continue
    pos[this_direction] += val

pos_north = abs(pos[NORTH] - pos[SOUTH])
pos_east = abs(pos[EAST] - pos[WEST])
print(pos_east + pos_north)
# > 2867

## PART B
waypoint = [1,10]
ship = [0,0]
for line in lines:
    this_direction = direction
    val = int(line[1:])
    if line.startswith("F"):
        ship[0] += waypoint[0] * val
        ship[1] += waypoint[1] * val
    elif line.startswith("N"):
        waypoint[0] += val
    elif line.startswith("E"):
        waypoint[1] += val
    elif line.startswith("S"):
        waypoint[0] -= val
    elif line.startswith("W"):
        waypoint[1] -= val
    else:
        direction = int(val/90)
        if line.startswith("L"):
            direction = 4-direction
        direction = direction % 4
        if direction == 1:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        if direction == 2:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        if direction == 3:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]


pos_north = abs(ship[0])
pos_east = abs(ship[1])
print(pos_east + pos_north)