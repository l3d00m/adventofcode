from aocd import get_data
lines = get_data(day=10, year=2020).splitlines()

from pathlib import Path
p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f: 
    lines = f.readlines()

lines = [line.replace("L","#") for line in lines]
    
def get_adjacent(x,y, this_item, lines, cnt=5):
    start_x = 0 if x-cnt-1 < 0 else x-cnt-1
    end_x = len(lines[y]) - 1 if x+cnt+1 >= len(lines[y]) else x+cnt+1
    start_y = 0 if y-cnt-1 < 0 else y-cnt-1
    end_y = len(lines) - 1 if y+cnt+1 >= len(lines) else y+cnt+1

    cnt = 0
    for this_y in range(start_y, end_y):
        diag_x1 = x + abs(this_y - y)
        diag_x2 = x - abs(this_y - y)
        for this_x in range(start_x, end_x):
            item = lines[this_y][this_x]
            if this_x == x and this_y == y:
                continue
            elif this_x == x and item == "#":
                cnt += 1
            elif this_y == y and item == "#":
                cnt += 1
            elif this_x == diag_x1 or this_x == diag_x2 and item == "#":
                cnt += 1

    return cnt

for y,line in enumerate(lines):
    for x, item in enumerate(line):
        if item != ".":
            get_adjacent(x,y, item, lines)