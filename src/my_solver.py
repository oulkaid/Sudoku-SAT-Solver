import sys
from util import *
from util2 import *

lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

n, grid = input_parser(lines)

print(">> Problem")
print_grid(grid, n)

# Running the algorithm
pre = []
pos = []
sol = find_solution(grid, n, 0, 0, pos, pre, 0)

print("\n>> Soltion")
print_grid(sol, n)
