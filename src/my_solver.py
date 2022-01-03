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

if check_init_integrity(grid, n) == True:
#solve sudoku:

    # 1.DONE: Find trivial solutions (cells with one single possible digit). Then move to backtracking algorithm
    grid, filled_cells = fill_trivial_cells(grid, n)
    '''
    if filled_cells > 0:
        print("\n>> Filling trivial cells")
        print_grid(grid, n)
    '''

    # TODO: in fact, this may shall be generalised, even when backtracking
    #       meaning that once we obtain a certain digit for some cell, we might run the trivial solutions finder
    
    
    # 2. Running the backtracking algorithm
    pre = []
    pos = []
    sol, finished, solved = find_solution(grid, n, 0, 0, pos, pre, 0)
    it = 0
    while not finished:
        it += 1
        if it%1000 == 0:
            logging.info(it)
            print(pos)
            print_grid(grid, n)
        sol, finished, solved = find_solution(sol, n, 0, 0, pos, pre, 0)

    if solved:
        print("\n>> Soltion")
        print_grid(sol, n)
    else:
        print("\n>> This is not a valid Sudoku problem!")

else:
    print("\n>> This is not a valid Sudoku problem!")
