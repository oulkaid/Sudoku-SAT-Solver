from math import sqrt
import logging
import sys
from utils import tools
from utils import algo
from utils import config
logging.basicConfig(level=logging.INFO)


lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

n, grid = tools.input_parser(lines)

print(">> Problem")
tools.print_grid(grid, n)

# Checking the integrity of the initial grid
if algo.check_integrity(grid, n) == True:
# Solve Sudoku:

    # Find initially blank squares
    algo.store_blank_squares(grid, n)

    # Running the backtracking algorithm
    pre = []
    pos = []
    sol, finished, solved = algo.find_solution(grid, n, 0, 0, pos, pre, 0)
    it = 0
    while not finished:
        it += 1
        if it%config.LOGGING_STEP == 0:
            logging.info("RECURSION RE-LAUNCH: " + str(it))
            tools.print_grid(grid, n)
        sol, finished, solved = algo.find_solution(sol, n, 0, 0, pos, pre, 0)

    if solved:
        print("\n>> Soltion")
        tools.print_grid(sol, n)
    else:
        print("\n>> (1) This is not a valid Sudoku problem!")

else:
    print("\n>> (2) This is not a valid Sudoku problem!")
