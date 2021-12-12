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
sol = find_solution(grid, n)

print("\n>> Soltion")
print_grid(sol, n)
