#application
import sys
from util import *
from util2 import *
import logging

logging.basicConfig(level=logging.DEBUG)

lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

n, grid = input_parser(lines)

print(">> Problem")
print_grid(grid, n)

# 1.DONE: Find trivial solutions (cells with one single possible digit). Then move to backtracking algorithm
grid = fill_trivial_cells(grid, n)
print("\n>> Mid-soltion")
print_grid(grid, n)
logging.info("finished filling trivial solutions")
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
