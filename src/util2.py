#algorithm
from util import *
from math import sqrt
import sys
import logging

RECURSION_LIMIT = sys.getrecursionlimit()-10
logging.basicConfig(level=logging.DEBUG)

def fill_trivial_cells(grid, n):
    filled = False
    filled_cells = 0
    while not filled:
        filled = True #hypothesis
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    possibilities = get_all_valid_digits_so_far(grid, n, i, j)
                    if len(possibilities) == 1:
                        grid[i][j] = possibilities[0]
                        filled = False
                        filled_cells += 1
                        #logging.info("grid:"+str(i)+","+str(j)) ##
    return grid, filled_cells


#FIXME: visiblement, there will be issues with first calls (especially when grid[0][0]==0)
#FIXME: pick some good heuristic to choose the next variable to assign. Otherwise, let it this way.
#DONE:One solution to solve this, is to break recursion after acheiving a certain number of calls, 
#       and resume with obtained state of parameters. So REPEAT until the sudoku is solved
COUNTER = RECURSION_LIMIT
def find_solution(grid, n, i, j, pos, pre, back_depth):
    global COUNTER
    COUNTER -= 1
    if (COUNTER == 0):
        COUNTER = RECURSION_LIMIT #RESET
        return grid, False, False
    
    if grid[i][j] == 0:
        #print_grid(grid, n) ##
        if [i,j] not in pre:
            pre.append([i,j])
            pos.append(0) #at first, try the very first possibility among possibilities
        digit = get_valid_digit(grid, n, i, j, pos[pre.index([i,j])])
        #print("-- "+str(i)+" "+str(j)) ##
        if digit == 0:
            #backtrack
            #print_grid(grid, n)
                # pre_i = pre[-2-back_depth][0] FIXME
                # pre_j = pre[-2-back_depth][1] FIXME
            pre_i = pre[pre.index([i,j])-1][0]
            pre_j = pre[pre.index([i,j])-1][1]
            #print("......... "+str(pre_i)+" "+str(pre_j)) ##
            #print("back_depth "+str(back_depth)) ##
            #print("pos "+str(pos)) ##
            grid[pre_i][pre_j] = 0
            pos[pre.index([pre_i,pre_j])] += 1 #FIXME don't forgot to reset the pos to zero, after re-taking the road
            #pos[pre.index([pre_i,pre_j])] %= len(get_all_valid_digits_so_far(grid, n, pre_i, pre_j)) #FIXES the above!
            #if we're heading up in depth, we shall reset the position to 1 (~pos+1-depth)
            # The follwing if statement means that if we repeat searching for solutions for a cell
            # repeatedly, this means that the search engine is stuck at this position. 
            # and that no other options are possible. Then, this only means UNSATISFIABLE PROBLEM!
            if pos[pre.index([pre_i,pre_j])] > len( get_all_valid_digits_so_far(grid, n, pre_i, pre_j) ):
                return grid, True, False
            return find_solution(grid, n, pre_i, pre_j, pos, pre, back_depth+1) #.. -back_depth ?
        else: #reset all the values after the barrier to zero #FIXES the above
            for e in range(pre.index([i,j])+1, len(pos)):
                pos[e] = 0
        
        grid[i][j] = digit
    
    if i == n-1 and j == n-1:
        return grid, True, True
    
    elif j == n-1:
        return find_solution(grid, n, i+1, 0, pos, pre, 0)
    else:
        return find_solution(grid, n, i, j+1, pos, pre, 0)


def get_valid_digit(sol, n, i, j, pos):
    possibilities = get_all_valid_digits_so_far(sol, n, i, j)
    #print("possibilities "+str(possibilities)) ##
    if len(possibilities) > pos:
        #print("selected "+str(possibilities[pos])) ##
        return possibilities[pos]
    else: return 0 #Here, when we get this 0 inside the find_solution, it'll backtrack to change the previous choice
                   #So the possibilities are being reminded through the simple `pos` index


def get_all_valid_digits_so_far(sol, n, i, j):
    possibilities = []
    for digit in range(1, n+1):
        if is_valid_digit(sol, n, i, j, digit):
            possibilities.append(digit)

    return possibilities
        

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

#checks the integrity of the initial grid: lines, cols, boxes
def check_init_integrity(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                if not is_valid_digit(grid, n, i, j, grid[i][j]):
                    return False
    
    return True
