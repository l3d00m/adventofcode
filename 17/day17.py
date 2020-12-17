import numpy as np
from pathlib import Path
from aocd import get_data
lines = get_data(day=17, year=2020).splitlines()

p = Path(__file__).resolve()
with open(p.parent / 'in.txt') as f:
    lines2 = f.read().splitlines()

iterations = 6
input_size = len(lines)
output_size = (iterations) * 2 + input_size

pocketdim = np.zeros((output_size, ) * 3, dtype=np.bool)
pocketdim4d = np.zeros((output_size, ) * 4, dtype=np.bool)

mid_i = output_size // 2
start_index = int((output_size - input_size) / 2)
end_index = start_index + input_size
for inner_i, outer_i in enumerate(range(start_index, end_index)):
    this_array = [char == "#" for char in lines[inner_i]]
    pocketdim[mid_i, outer_i, start_index:end_index] = this_array
    pocketdim4d[mid_i, mid_i, outer_i, start_index:end_index] = this_array


def get_index(index, mshape, dim):
    """Helper function to return a valid start and and index for the specified `dim`"""
    el = index[dim]
    start_el = el - 1 if el > 0 else 0
    end_el = el + 2 if el <= mshape[dim] else el
    return start_el, end_el


def get_active_neighbors_3d(index, matrix):
    """Returns the count of active (= True) neighbors in a 3d matrix"""
    start_z, end_z = get_index(index, matrix.shape, 0)
    start_y, end_y = get_index(index, matrix.shape, 1)
    start_x, end_x = get_index(index, matrix.shape, 2)
    submatrix = matrix[start_z:end_z, start_y:end_y, start_x:end_x]
    cnt = np.count_nonzero(submatrix == True)
    return cnt


def get_active_neighbors_4d(index, matrix):
    """Pretty much the same as the 3d function, except that we use one dimensions more"""
    start_w, end_w = get_index(index, matrix.shape, 0)
    start_z, end_z = get_index(index, matrix.shape, 1)
    start_y, end_y = get_index(index, matrix.shape, 2)
    start_x, end_x = get_index(index, matrix.shape, 3)
    submatrix = matrix[start_w:end_w, start_z:end_z, start_y:end_y, start_x:end_x]
    cnt = np.count_nonzero(submatrix == True)
    return cnt


# Loop for Part A
for _ in range(6):
    pocketdim_old = pocketdim.copy()
    for index, el in np.ndenumerate(pocketdim_old):
        active_cnt = get_active_neighbors_3d(index, pocketdim_old)
        if el and active_cnt not in [3, 4]:
            pocketdim[index] = False
        if not el and active_cnt == 3:
            pocketdim[index] = True
    continue
total_cnt = np.count_nonzero(pocketdim == True)
print(total_cnt)


# Loop for Part B
for i2 in range(6):
    pocketdim_old = pocketdim4d.copy()
    # This loop is a little bit inefficient,
    # since we are comparing every element even in the first loops. Still runs fast enough though
    for index, el in np.ndenumerate(pocketdim_old):
        active_cnt = get_active_neighbors_4d(index, pocketdim_old)
        if el and active_cnt not in [3, 4]:
            pocketdim4d[index] = False
        if not el and active_cnt == 3:
            pocketdim4d[index] = True
    continue
total_cnt = np.count_nonzero(pocketdim4d == True)
print(total_cnt)
