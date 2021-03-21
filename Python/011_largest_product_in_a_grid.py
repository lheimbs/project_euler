import sys
import numpy as np


if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    N = int(sys.argv[1])
else:
    N = 4

grid = []
with open('grid.txt', 'r') as grid_file:
    for line in grid_file.readlines():
        grid.append([int(num) for num in line.split(' ')])
        # print(grid[-1])
grid_np = np.array(grid)
max_row, max_col = grid_np.shape

def get_prod(N):
    max_prod = 0
    max_row = len(grid) - N
    for row in range(0, len(grid)):
        max_col = len(grid[row]) - N
        for col in range(0, len(grid[row])):
            # vertical
            if col <= max_col:
                prod = np.prod(grid[row][col:col+N])
                if prod > max_prod:
                    max_prod = prod
            # horizontal
            if row <= max_row:
                prod = np.prod(grid_np[row:row+N,col])
                if prod > max_prod:
                    max_prod = prod
            # diagonal down->up
            if row >= N and col <= max_col:
                grid_sel = grid_np[row-N:row,col:col+N]
                prod = np.prod(np.flipud(grid_sel).diagonal())
                if prod > max_prod:
                    max_prod = prod
            # diagonal up->down
            if row <= max_row and col <= max_col:
                prod = np.prod(grid_np[row:].diagonal(col)[:N])
                if prod > max_prod:
                    max_prod = prod
    return max_prod

print(get_prod(N))

