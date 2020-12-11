from pathlib import Path
from aocd import get_data
lines = get_data(day=11, year=2020).splitlines()

p = Path(__file__).resolve()
# with open(p.parent / 'in.txt') as f:
#    lines = f.read().splitlines()

# lines = [line.replace("L","#") for line in lines]


def get_adjacent_a(x, y, this_item, lines):
    start_x = 0 if x-1 < 0 else x-1
    end_x = len(lines[y]) if x+2 >= len(lines[y]) else x+2
    start_y = 0 if y-1 < 0 else y-1
    end_y = len(lines) if y+2 >= len(lines) else y+2

    cnt = sum([line[start_x:end_x].count("#") for line in lines[start_y:end_y]])
    if this_item == '#':
        cnt -= 1
    return cnt


end_layout = lines.copy()
prev_layout = []
while end_layout != prev_layout:
    prev_layout = end_layout.copy()
    for y, line in enumerate(end_layout):
        for x, item in enumerate(line):
            if item != ".":
                adjacent_cnt = get_adjacent_a(x, y, item, prev_layout)
                if item == "#" and adjacent_cnt >= 4:
                    end_layout[y] = end_layout[y][:x] + "L" + end_layout[y][x + 1:]
                elif item == "L" and adjacent_cnt == 0:
                    end_layout[y] = end_layout[y][:x] + "#" + end_layout[y][x + 1:]

cnt = sum([line.count("#") for line in end_layout])
print(cnt)
pass


# Part B

def walk(x, y, dx, dy, lines):
    while 1:
        x = x + dx
        y = y + dy
        if x < 0 or x > len(lines[0]) - 1:
            return False
        if y < 0 or y > len(lines) - 1:
            return False
        if lines[y][x] == "L":
            return False
        if lines[y][x] == "#":
            return True


def get_adjacent_b(x, y, this_item, lines):
    cnt = 0
    cnt += walk(x, y, 0, 1, lines)
    cnt += walk(x, y, 0, -1, lines)
    cnt += walk(x, y, 1, 0, lines)
    cnt += walk(x, y, -1, 0, lines)
    cnt += walk(x, y, 1, 1, lines)
    cnt += walk(x, y, 1, -1, lines)
    cnt += walk(x, y, -1, 1, lines)
    cnt += walk(x, y, -1, -1, lines)
    # print("xxxxxx")
    return cnt


end_layout = lines.copy()
prev_layout = []
while end_layout != prev_layout:
    prev_layout = end_layout.copy()
    for y, line in enumerate(end_layout):
        for x, item in enumerate(line):
            if item != ".":
                adjacent_cnt = get_adjacent_b(x, y, item, prev_layout)
                if item == "#" and adjacent_cnt >= 5:
                    end_layout[y] = end_layout[y][:x] + "L" + end_layout[y][x + 1:]
                elif item == "L" and adjacent_cnt == 0:
                    end_layout[y] = end_layout[y][:x] + "#" + end_layout[y][x + 1:]

cnt = sum([line.count("#") for line in end_layout])
print(cnt)
pass
