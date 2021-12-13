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

# Running the algorithm
pre = []
pos = []
sol, solved = find_solution(grid, n, 0, 0, pos, pre, 0)
it = 0
while not solved:
    it += 1
    if it%10000 == 0:
        logging.info(it)
        print(pos)
        print_grid(grid, n)
    sol, solved = find_solution(sol, n, 0, 0, pos, pre, 0)


print("\n>> Soltion")
print_grid(sol, n)
