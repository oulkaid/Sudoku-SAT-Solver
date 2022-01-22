from math import sqrt
import copy
import sys
from utils import tools
from utils import config

log_file = open("trace.log","w")
old_stdout = sys.stdout


COUNTER = config.RECURSION_LIMIT
def find_solution(grid, n, i, j, pos, pre, back_depth):
    global COUNTER
    COUNTER -= 1
    if (COUNTER == 0):
        COUNTER = config.RECURSION_LIMIT #RESET COUNTER
        return grid, False, False
    
    if grid[i][j] == 0: #blank square
        if [i,j] not in pre:
            pre.append([i,j])
            pos.append(0) #first, try the very first possibility among `possibilities`

        log("\nactual-square:("+str(i)+","+str(j)+")")
        digit = get_valid_digit(grid, n, i, j, pos[pre.index([i,j])])
        if digit == 0:
            #backtrack (if possible):
            pre_i = pre[pre.index([i,j])-1][0]
            pre_j = pre[pre.index([i,j])-1][1]
            log("back-to-square:("+str(pre_i)+","+str(pre_j)+")")
            log("back-depth:"+str(back_depth)) 
            grid[pre_i][pre_j] = 0
            pos[pre.index([pre_i,pre_j])] += 1

            # The follwing if statement means that if we repeat searching for solutions for a square
            # repeatedly, this means that the search engine is stuck at this position, an that
            # no other options are possible. Then, this only means UNSATISFIABLE PROBLEM:
            if pos[pre.index([pre_i,pre_j])] > len( get_all_valid_digits_so_far(grid, n, pre_i, pre_j) ):
                log_file.close()
                return grid, True, False #unsatisfiable
            # backtrack:
            return find_solution(grid, n, pre_i, pre_j, pos, pre, back_depth+1)
        else: 
            # RESET all `pos` indexes to zero after resuming forward search:
            for e in range(pre.index([i,j])+1, len(pos)):
                pos[e] = 0
        
        grid[i][j] = digit
    
    if i == n-1 and j == n-1:
        # Sudoku solved
        log_file.close()
        return grid, True, True

    else:
        square = get_next_blank_square(i, j)
        if square != -1:
            # `square` is of the format [i,j]
            return find_solution(grid, n, square[0], square[1], pos, pre, 0)
        else:
            # Sudoku solved
            log_file.close()
            return grid, True, True


def store_blank_squares(grid, n):
    global blank_squares
    blank_squares = []

    # add first grid square even if is initially filled. This is to avoid handling the existing or not of this square digit
    if grid[0][0] != 0:
        blank_squares.append([0,0])

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                blank_squares.append([i,j])


def get_next_blank_square(i, j):
    index_i_j = blank_squares.index([i,j])
    if len(blank_squares) > index_i_j + 1:
        return blank_squares[index_i_j+1]
    else:
        # reached the end of blank squares list
        return -1


def get_valid_digit(sol, n, i, j, pos):
    possibilities = get_all_valid_digits_so_far(sol, n, i, j)
    log("possibilities:"+str(possibilities)) 
    if len(possibilities) > pos:
        log("picked-digit:"+str(possibilities[pos])) 
        return possibilities[pos]
    else: return 0 


def get_all_valid_digits_so_far(sol, n, i, j):
    possibilities = []
    for digit in range(1, n+1):
        if is_valid_digit(sol, n, i, j, digit):
            possibilities.append(digit)

    return possibilities
        

# Checking the integrity of the grid in the presence of `digit` in square (i,j)
def is_valid_digit(sol, n, i, j, digit):
    #checking the line
    for pos_j in range(n):
        if pos_j != j:
            if sol[i][pos_j] == digit:
                return False
    #checking the column
    for pos_i in range(n):
        if pos_i != i:
            if sol[pos_i][j] == digit:
                return False
    #checking the box (for n=9, the box itself is recongnized by int(i/3),int(j/3))
    base_box_i = int(sqrt(n))*int(i/int(sqrt(n)))
    base_box_j = int(sqrt(n))*int(j/int(sqrt(n)))
    for ii in range(int(sqrt(n))):
        index_ii = base_box_i + ii%int(sqrt(n))
        for jj in range(int(sqrt(n))):
            index_jj = base_box_j + jj%int(sqrt(n))
            if index_ii != i and index_jj != j:
                if sol[index_ii][index_jj] == digit:
                    return False
    
    return True


# Checks the integrity of the grid: lines, cols, boxes
def check_integrity(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                if not is_valid_digit(grid, n, i, j, grid[i][j]):
                    return False
    
    return True


def log(message):
    sys.stdout = log_file
    print(message)
    sys.stdout = old_stdout
