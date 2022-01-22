from z3 import *
from math import sqrt
import sys
from utils import tools

lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

n, grid = tools.input_parser(lines)

print(">> Problem")
tools.print_grid(grid, n)

# Create a Solver Object
s = Solver()

# Initialize solution vector
sol = [ Int(f"s{tools.int_to_hex(i)}_{tools.int_to_hex(j)}") for i in range(n) for j in range(n) ]

# Specify initial values of the sudoku problem as defined in the grid
grid_elements = [ If(grid[int(i/n)][i%n] == 0,
                        True,
                        sol[i] == grid[int(i/n)][i%n])
                    for i in range(n*n) ]
s.add(grid_elements)

# `sol` values must be contained in [1,n]
valid_range_val = [ And(1 <= sol[i], sol[i] <= n) for i in range(n*n) ]
s.add(valid_range_val)

# Distinct values in each line
dist_line_val = [ If(i == ii,
                        True,
                        sol[i+n*line] != sol[ii+n*line])
                    for line in range(n) for i in range(n) for ii in range(n) ]
s.add(dist_line_val)

# Distinct values in each column
dist_col_val = [ If(j == jj,
                        True,
                        sol[n*j+col] != sol[n*jj+col])
                    for col in range(n) for j in range(n) for jj in range(n) ]
s.add(dist_col_val)

# Distinct values in each box
box_index = []
for box_i in range(int(sqrt(n))):
    for box_j in range(int(sqrt(n))):
        box_index.append(n*int(sqrt(n))*box_i + int(sqrt(n))*box_j)
for box in range(n):
    for item in range(n):
        for ii in range(item+1, n):
            s.add(                                                                      \
                sol[box_index[box] + ii%int(sqrt(n)) + n*int(ii/int(sqrt(n)))] !=       \
                sol[box_index[box] + item%int(sqrt(n)) + n*int(item/int(sqrt(n)))] )

# Check satisfiability
satResult = s.check()
print(satResult)

# If satisfiable, then print solution
if (satResult == z3.sat):
    m = s.model()
    m_sorted_tmp = sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))
    m_sorted = []
    for i in range(n*n):
        m_sorted.append(m_sorted_tmp[i][1])

    print("\n>> Solution")
    tools.print_solution(m_sorted, n)
