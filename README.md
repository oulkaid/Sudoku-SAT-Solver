# Sudoku Solver
> Author: Oussama Oulkaid

## Environment
To run the tools you need:
- Python3 (tested with version 3.8.10)
- Python packages: `z3`, `math`, `sys`, `logging`, `copy`

## 1. Running the tools

### 1.1. Z3 Based Solver: `src/s3_solver.py`
To solve a Sudoku problem using the *Z3 based Solver*, run the following command:

    python3 src/z3_solver.py samples/{GRID_X}.txt

Where `{GRID_X}.txt` denotes the name of the file containing the Sudoku problem to be solved. Examples are provided inside folder `samples/`.

For Example:

    python3 src/z3_solver.py samples/grid_9.txt

This will tell if the problem is satisfiable. If yes, it will print a solution.

### 1.2. Backtracking Based Solver: `src/backtrack_solver.py`
Similarly, to use this solver, run the following command:

    python3 src/backtrack_solver.py samples/{GRID_X}.txt

Where `{GRID_X}.txt` denotes the name of the file containing the Sudoku problem to be solved.

A trace will be generated (file `trace.log`). It contains the search history performed by the tool.
The program terminates by either giving a solution, or by reporting that the input is not a Sudoku problem.

> For a detailed documentation about these tools, you can refer to [`doc/manual.pdf`](https://github.com/oulkaid/Sudoku-SAT-Solver/tree/main/doc/manual.pdf).
