import random
from util import *
from util2 import *

n = 9
grid = []
for i in range(n):
    grid.append([0]*n)

for i in range(n):
    for j in range(n):
        # let's fill 1/3 cells of the grid with random {valid} digits (so far)
        pick = random.randint(1,9)
        if pick == 1:
            filled = False
            attempts = 10
            while not(filled) and attempts > 0:
                attempts -= 1
                digit = random.randint(1,n)
                if is_valid_digit(grid, n, i, j, digit):
                    grid[i][j] = digit
                    filled = True

print("\n>> Initiate Problem")
print_grid(grid, n)







# 1.DONE: Find trivial solutions (cells with one single possible digit). Then move to backtracking algorithm
grid, filled_cells = fill_trivial_cells(grid, n)
if filled_cells > 0:
    print("\n>> Filling trivial cells")
    print_grid(grid, n)

# TODO: in fact, this shall be generalised, even when backtracking
#       meaning that once we obtain a certain digit for some cell, we might run the trivial solutions finder

# 2. Running the backtracking algorithm
pre = []
pos = []
sol, solved = find_solution(grid, n, 0, 0, pos, pre, 0)
it = 0
while not solved:
    it += 1
    if it%1000 == 0:
        logging.info(it)
        print(pos)
        print_grid(grid, n)
    sol, solved = find_solution(sol, n, 0, 0, pos, pre, 0)



print("\n>> Soltion")
print_grid(sol, n)
