from z3 import *

def print_sudoku(board): #not used
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")

def print_solution_old(m): #not used
   for line in range(9):
      for i in range(9):
         print(str(m[m.decls()[i+9*line]]) + " ", end="")  
         if (i+1)%3 == 0:
            print(" ", end="")
      print()
      if (line+1)%3 == 0:
          print()

def print_solution(m):
   for i in range(9*9):
        print( str(m[i]) + " ", end="")  
        if (i+1)%(9*3) == 0:
            print("\n")
        elif (i+1)%9 == 0:
            print("")
        elif (i+1)%3 == 0:
            print(" ", end="")


grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

print("\n------PROBELM------")
print(grid)

sol = [ Int(f"s{i}_{j}") for i in range(9) for j in range(9) ]

# Distinct values in each line
dist_line_val = [ If(i == ii,
                        True,
                        sol[i+9*line] != sol[ii+9*line])
                    for line in range(9) for i in range(9) for ii in range(9) ]

# Distinct values in each column
dist_col_val = [ If(j == jj,
                        True,
                        sol[9*j+col] != sol[9*jj+col])
                    for col in range(9) for j in range(9) for jj in range(9) ]

# sol values must be contained within [1,9]
valid_range_val = [ And(1 <= sol[i], sol[i] <= 9) for i in range(9*9) ]

# specify initial values of the sudoku problem as defined in the grid (depricated)
# for i in range(9):
    # for j in range(9):
        # if grid[i][j] != 0:
            # s.add( sol[i][j] == grid[i][j] )

# specify initial values of the sudoku problem as defined in the grid
grid_elements = [ If(grid[int(i/9)][i%9] == 0,
                        True,
                        sol[i] == grid[int(i/9)][i%9])
                    for i in range(9*9) ]

# TODO: ensure uniqueness of values in each box
dist_box_val = []

s = Solver()
s.add(dist_line_val)
s.add(dist_col_val)
s.add(valid_range_val)
s.add(grid_elements)
print(s.check())
m = s.model()

m_sorted_tmp = sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))
m_sorted = []
for i in range(9*9):
    m_sorted.append(m_sorted_tmp[i][1])

print("\n------SOLUTION------")
print_solution(m_sorted)
