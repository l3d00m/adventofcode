from pathlib import Path
from aocd import get_data
import numpy as np
lines = get_data(day=20, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

tiles = {}
this_id = -1
current_tile = []
for line in lines:
    if line == "":
        continue
    elif line.startswith("Tile "):
        if len(current_tile) > 0:
            tiles[this_id] = np.array(current_tile)
            current_tile = []
        this_id = int(line[len("Tile "):-1])
    else:
        current_row = [c == "#" for c in line]
        current_tile.append(current_row)
tiles[this_id] = np.array(current_tile)

tile_num = len(tiles)
import math
border_len = int(math.sqrt(tile_num))
single_tile_len = len(current_tile)

borders = {}
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def get_border_of_tile(tile, location):
    if location == NORTH:
        return tile[0, :]
    if location == EAST:
        return tile[:, -1]
    if location == SOUTH:
        return tile[-1, :]
    if location == WEST:
        return tile[:, 0]


for tileid, tile in tiles.items():
    border = np.zeros((4, len(tile[0])), dtype=np.bool)
    border[NORTH] = get_border_of_tile(tile, NORTH)
    border[EAST] = get_border_of_tile(tile, EAST)
    border[SOUTH] = get_border_of_tile(tile, SOUTH)
    border[WEST] = get_border_of_tile(tile, WEST)
    borders[tileid] = border


def match_borders_only(borders1, borders2, borderloc):
    ref = borders1[borderloc]
    for i in range(4):
        borders2 = np.roll(borders2, 1, axis=0)
        if np.sum(ref) != np.sum(borders2[0]):
            continue
        if (ref == borders2[0]).all():
            return True
        borders2 = np.fliplr(borders2)
        if (ref == borders2[0]).all():
            return True
    return False


corners = []
for ref_id, ref in borders.items():
    #print(f"\n Base Element: {ref_id}")
    match_counter = 0
    for compare_id, border in borders.items():
        if compare_id == ref_id:
            continue
        for border_i in range(4):
            if match_borders_only(ref, border, border_i):
                #print(f"{compare_id} on border orientation {border_i}")
                match_counter += 1
                break
        if match_counter > 2:
            break
    if match_counter == 2:
        corners.append(ref_id)
mul = 1
for el in corners:
    mul *= el
print(mul)


### PART B


def match_tile(current_tile, compare_tile, relevant_orientation):
    ref = get_border_of_tile(current_tile, relevant_orientation)
    orientation = (relevant_orientation + 2) % 4
    for i in range(2):
        for i in range(4):
            comp = get_border_of_tile(compare_tile, orientation)
            if (ref == comp).all():
                return compare_tile
            compare_tile = np.rot90(compare_tile)
        compare_tile = np.fliplr(compare_tile)
    return None


def get_next(current_tile, current_id, orientation, tiles):
    for compare_id, compare_tile in tiles.items():
        if compare_id == current_id:
            continue
        next_tile = match_tile(current_tile, compare_tile, orientation)
        if next_tile is not None:
            return compare_id, next_tile
    return None


def get_start_tile(corners):
    for start_id in corners:
        start_tile = tiles[start_id]
        for _ in range(2):
            for _ in range(4):
                if get_next(start_tile, start_id, EAST, tiles) is not None:
                    if get_next(start_tile, start_id, SOUTH, tiles) is not None:
                        return start_id, start_tile
                start_tile = np.rot90(start_tile)
            start_tile = np.fliplr(start_tile)


result = []
result_id, result_tile = get_start_tile(corners)
last_start_id = result_id
last_start_tile = result_tile
del tiles[result_id]
for column_i in range(border_len):
    row_vector = []
    for row_i in range(border_len - 1):
        prev_id, prev_tile = result_id, result_tile
        row_vector.append(prev_tile[1:-1, 1:-1])
        result_id, result_tile = get_next(prev_tile, prev_id, EAST, tiles)
        del tiles[result_id]

    row_vector.append(result_tile[1:-1, 1:-1])
    result.append(np.hstack(row_vector))
    if column_i == border_len - 1:
        break
    result_id, result_tile = get_next(last_start_tile, last_start_id, SOUTH, tiles)
    del tiles[result_id]
    last_start_id = result_id
    last_start_tile = result_tile

image = np.vstack(result).astype(int)

monster_str = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
monster = [[1 if c == "#" else 0 for c in line] for line in monster_str]
monster_len = np.count_nonzero(monster)

from scipy.ndimage import convolve
for i in range(2):
    for i in range(4):
        masked = convolve(image, monster, mode='constant', cval=0.0)
        monster_cnt = np.count_nonzero(masked == monster_len)
        if monster_cnt > 0:
            res = np.count_nonzero(image == 1) - monster_cnt * monster_len
            print(res)
            break
        image = np.rot90(image)
    image = np.fliplr(image)

pass
