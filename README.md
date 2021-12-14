# Sudoku-SAT-Solver
> Author: Oussama Oulkaid

## Roadmap
- [x] Build a Sudoku solver
- [x] Write my own solving algorithm through backtracking
    - [ ] Implement some good heuristics for picking the next digit
    - [ ] Maybe combine with other techniques
    - [ ] Optimize the overall implementation

## Running the z3 based solver
Run the following command:

    python3 src/z3_solver.py inputs/{INPUT_X}.txt

Where `{INPUT_X}.txt` denotes the file containing the Sudoku problem to be solved. 

For Example:

    python3 src/z3_solver.py inputs/input_9.txt

## Running my personal solver
Run the following command (you might want to redirect the search trace to a log file):

    python3 src/my_solver.py inputs/{INPUT_X}.txt > {TRACE_NAME}.log

For Example:

    python3 src/my_solver.py inputs/input_9.txt > trace.log

Otherwise, you can discard the trace by redirecting the output to the null device of your operating system (especially when expecting a huge trace size that might cause a storage issue). 
For Ubuntu it's `/dev/null`.

    python3 src/my_solver.py inputs/input_9.txt > /dev/null
