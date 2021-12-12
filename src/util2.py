from math import sqrt

def find_solution(grid, n):
    sol = grid
    for i in range(n):
        for j in range(n):
            if sol[i][j] == 0:
                sol[i][j] = get_valid_digit(sol, n, i, j)
                #FIXME: here, we have to go back in indexes i,j (backtrack) when we're stuck
                #maybe, we can indicate which choice to take by using some global variable
                #we'll certainly need a way to remind the last filled cell, so that we can restart from there
                #some recursion is required. think about it!

    return sol


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
