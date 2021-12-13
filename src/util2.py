#algorithm
from util import *
from math import sqrt
import sys
#sys.setrecursionlimit(30000)
RECURSION_LIMIT = sys.getrecursionlimit()-10

#visiblement, there will be issues with first calls (especially when grid[0][0]==0) FIXME:
#TODO:One way to check if works for larger grids <functionally> is to fill make the problem easier
#TODO:One solution to solve this, is to break recursion after acheiving a certain number of calls, 
#       and resume with obtained state of parameters. So REPEAT until the sudoku is solved
COUNTER = RECURSION_LIMIT
def find_solution(grid, n, i, j, pos, pre, back_depth):
    global COUNTER
    COUNTER -= 1
    if (COUNTER == 0):
        COUNTER = RECURSION_LIMIT #RESET
        return grid, False
    
    if grid[i][j] == 0:
        #print_grid(grid, n) #TODO:UNCOMMENT
        if [i,j] not in pre:
            pre.append([i,j])
            pos.append(0) #at first, try the very first possibility among possibilities
        digit = get_valid_digit_bis(grid, n, i, j, pos[pre.index([i,j])])
        #print("-- "+str(i)+" "+str(j)) #TODO:UNCOMMENT
        if digit == 0:
            #backtrack
            #print_grid(grid, n)
                # pre_i = pre[-2-back_depth][0] FIXME
                # pre_j = pre[-2-back_depth][1] FIXME
            pre_i = pre[pre.index([i,j])-1][0]
            pre_j = pre[pre.index([i,j])-1][1]
            #print("......... "+str(pre_i)+" "+str(pre_j)) #TODO:UNCOMMENT
            #print("back_depth "+str(back_depth)) #TODO:UNCOMMENT
            #print("pos "+str(pos)) #TODO:UNCOMMENT
            grid[pre_i][pre_j] = 0
            pos[pre.index([pre_i,pre_j])] += 1 #FIXME don't forgot to reset the pos to zero, after re-taking the road
            #pos[pre.index([pre_i,pre_j])] %= len(get_all_valid_digits_so_far(grid, n, pre_i, pre_j)) #FIXES the above!
            #if we're heading up in depth, we shall reset the position to 1 (~pos+1-depth)
            return find_solution(grid, n, pre_i, pre_j, pos, pre, back_depth+1) #.. -back_depth ?
        else: #reset all the values after the barrier to zero #FIXES the above
            for e in range(pre.index([i,j])+1, len(pos)):
                pos[e] = 0
        
        grid[i][j] = digit
    
    if i == n-1 and j == n-1:
        return grid, True
    
    elif j == n-1:
        return find_solution(grid, n, i+1, 0, pos, pre, 0)
    else:
        return find_solution(grid, n, i, j+1, pos, pre, 0)


def get_valid_digit_bis(sol, n, i, j, pos):
    possibilities = get_all_valid_digits_so_far(sol, n, i, j)
    #print("possibilities "+str(possibilities)) #TODO:UNCOMMENT
    if len(possibilities) > pos:
        #print("selected "+str(possibilities[pos])) #TODO:UNCOMMENT
        return possibilities[pos] #just randomly getting a value FIXME:
    else: return 0 #here, I shall backtrack to change the previous choice TODO:
                   #IDEA1: use another triple vector to store possibilities

# def find_solution(grid, n):
#     sol = grid
#     i = 0
#     j = 0
#     backtrack = False
#     while i < n:
#         while j < n:
#             backtrack = False
#             if sol[i][j] == 0:
#                 sol[i][j] = get_valid_digit(sol, n, i, j)
#                 #FIXME: here, we have to go back in indexes i,j (backtrack) when we're stuck
#                 #maybe, we can indicate which choice to take by using some global variable
#                 #we'll certainly need a way to remind the last filled cell, so that we can restart from there
#                 #some recursion is required. think about it!
#                 if get_valid_digit(sol, n, i, j) == 0:
#                     i = last_i
#                     j = last_j
#                     backtrack = True
#                     #print("backtrack to: "+str(i) + " " +str(j))

#                 last_i = i
#                 last_j = j
            
#             if not backtrack:
#                 j += 1
#         if not backtrack:
#             i += 1

#     return sol

# def find_solution(grid, n):
#     sol = grid
#     for i in range(n):
#         for j in range(n):
#             if sol[i][j] == 0:
#                 sol[i][j] = get_valid_digit(sol, n, i, j)
#                 #FIXME: here, we have to go back in indexes i,j (backtrack) when we're stuck
#                 #maybe, we can indicate which choice to take by using some global variable
#                 #we'll certainly need a way to remind the last filled cell, so that we can restart from there
#                 #some recursion is required. think about it!
#                 if get_valid_digit(sol, n, i, j) == 0:
#                     i = last_i
#                     j = last_j

#                 last_i = i
#                 last_j = j

#     return sol


def get_valid_digit(sol, n, i, j):
    possibilities = get_all_valid_digits_so_far(sol, n, i, j)
    if len(possibilities) > 0:
        return possibilities[0] #just randomly getting a value FIXME:
    else: return 0 #here, I shall backtrack to change the previous choice TODO:
                   #IDEA1: use another triple vector to store possibilities
    

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
