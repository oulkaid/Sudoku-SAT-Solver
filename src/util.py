from math import sqrt

def input_parser(lines):
    n = int(lines[0])
    grid = []
    for i in range(1, len(lines)):
        item = 0
        end_of_line = False
        new_line = []
        while not end_of_line:
            if lines[i][item] == '\n':
                end_of_line = True
            elif lines[i][item] == ' ':
                pass
            elif lines[i][item] == '-' or lines[i][item] == '_':
                new_line.append(0)
            elif (lines[i][item] >= 'A' and lines[i][item] <= 'P') or (lines[i][item] >= 'a' and lines[i][item] <= 'p'):
                new_line.append( hex_to_int( lines[i][item] ) )
            elif int(lines[i][item]) <= n and int(lines[i][item]) > 0:
                new_line.append(int(lines[i][item]))

            item += 1   
            if len(new_line) == n:
                end_of_line = True
        
        if len(new_line) == n:
            grid.append(new_line)
    
    return n, grid


def hex_to_int(c):
    if c == 'A' or c == 'a':
        return 10
    elif c == 'B' or c == 'b':
        return 11
    elif c == 'C' or c == 'c':
        return 12
    elif c == 'D' or c == 'd':
        return 13
    elif c == 'E' or c == 'e':
        return 14
    elif c == 'F' or c == 'f':
        return 15
    elif c == 'G' or c == 'g':
        return 16
    elif c == 'H' or c == 'h':
        return 17
    elif c == 'I' or c == 'i':
        return 18
    elif c == 'J' or c == 'j':
        return 19
    elif c == 'K' or c == 'k':
        return 20
    elif c == 'L' or c == 'l':
        return 21
    elif c == 'M' or c == 'm':
        return 22
    elif c == 'N' or c == 'n':
        return 23
    elif c == 'O' or c == 'o':
        return 24
    elif c == 'P' or c == 'p':
        return 25


def int_to_hex(n):
    if n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    elif n == 16:
        return 'G'
    elif n == 17:
        return 'H'
    elif n == 18:
        return 'I'
    elif n == 19:
        return 'J'
    elif n == 20:
        return 'K'
    elif n == 21:
        return 'L'
    elif n == 22:
        return 'M'
    elif n == 23:
        return 'N'
    elif n == 24:
        return 'O'
    elif n == 25:
        return 'P'
    else: return n


def print_grid(grid, n):
    print("+" + ("-"*(int(sqrt(n))*2+1) + "+")*int(sqrt(n)))
    for i, row in enumerate(grid):
        if (n == 4):
            print(("|" + " {} {} |"*int(sqrt(n))).format(*[x if x != 0 else "." for x in row]))
        elif (n == 9):
            print(("|" + " {} {} {} |"*int(sqrt(n))).format(*[x if x != 0 else "." for x in row]))
        elif (n == 16):
            print(("|" + " {} {} {} {} |"*int(sqrt(n))).format(*[int_to_hex(x) if x != 0 else "." for x in row]))
        elif (n == 25):
            print(("|" + " {} {} {} {} {} |"*int(sqrt(n))).format(*[int_to_hex(x) if x != 0 else "." for x in row]))
        
        if i == n:
            print("+" + ("-"*(int(sqrt(n))*2+1) + "+")*int(sqrt(n)))
        elif i % int(sqrt(n)) == int(sqrt(n))-1:
            print("+" + ("-"*(int(sqrt(n))*2+1) + "+")*int(sqrt(n)))


def print_solution(m, n):
    print("+" + ("-"*(int(sqrt(n))*2+1) + "+")*int(sqrt(n)))
    for i in range(n*n):
        if i%n == 0:
            print("| ", end="")

        if (n == 16 or n == 25):
            print( str(int_to_hex(m[i])) + " ", end="" )
        else:
            print( str(m[i]) + " ", end="" )

        if (i+1)%(n*int(sqrt(n))) == 0:
            print("|\n+" + ("-"*(int(sqrt(n))*2+1) + "+")*int(sqrt(n)))
        elif (i+1)%n == 0:
            print("|")
        elif (i+1)%int(sqrt(n)) == 0:
            print("| ", end="")

def print_solution_REPLICATED(m, n):
    for i in range(n*n):
        print( str(m[i]) + " ", end="")  
        if (i+1)%(n*int(sqrt(n))) == 0:
            print("\n")
        elif (i+1)%n == 0:
            print("")
        elif (i+1)%int(sqrt(n)) == 0:
            print(" ", end="")

