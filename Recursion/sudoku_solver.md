# Problem 
https://leetcode.com/problems/sudoku-solver/description/

# Brute force
# Intuition
The initial thought is to use a backtracking algorithm to solve the Sudoku puzzle. The idea is to try placing each number (1-9) in every empty cell and recursively attempt to solve the board. If a number placement leads to a valid solution, we proceed; otherwise, we backtrack and try the next number.

# Approach
1. Iterate through each cell in the board.
2. For each empty cell, try placing numbers from 1 to 9.
3. Use a helper function `is_valid` to check if placing a number in a cell is valid.
4. If a valid number is found, place it and recursively attempt to solve the rest of the board.
5. If placing a number leads to a dead end, backtrack by resetting the cell and trying the next number.
6. Continue this process until the board is completely filled or no valid placements are possible.

# Complexity
- Time complexity: 
  The worst-case time complexity is $$O(9^{81})$$ due to the nature of the backtracking algorithm, where each of the 81 cells can have 9 possible numbers.
- Space complexity: 
  The space complexity is $$O(1)$$ as the board is modified in place and no additional data structures are used.
# Code
```python3 []
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(num, row, column):
            for i in range(9):
                if board[row][i] == num or board[i][column] == num:
                    return False
                if board[(row // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == num:
                    return False
            return True

        def solve_sudoku():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            if is_valid(k, i, j):
                                board[i][j] = k
                                if solve_sudoku():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve_sudoku()
        return board
```

# Optimized Solution with MRV(Minimum Remaining Values ) Heuristic
# Intuition
To improve the performance of the Sudoku solver, we can use the Minimum Remaining Values (MRV) heuristic. The idea is to select the cell with the fewest possible values first, reducing the search space and leading to faster conflict detection and resolution.

# Approach
1. Implement a `find_empty` function to identify the empty cell with the fewest valid options.
2. Use the `is_valid` function to check if placing a number in a cell is valid.
3. Modify the `solve_sudoku` function to use the cell identified by `find_empty` for placing numbers.
4. For each empty cell, try placing numbers from 1 to 9.
5. If a valid number is found, place it and recursively attempt to solve the rest of the board.
6. If placing a number leads to a dead end, backtrack by resetting the cell and trying the next number.
7. Continue this process until the board is completely filled or no valid placements are possible.

# Complexity
- Time complexity: 
  The worst-case time complexity remains $$O(9^{81})$$, but the MRV heuristic significantly reduces the number of recursive calls in practice by focusing on the most constrained cells first.
- Space complexity: 
  The space complexity is $$O(1)$$ as the board is modified in place and no additional data structures are used.

# Code
```python3 []
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, row, column):
            for i in range(9):
                if board[row][i] == num or board[i][column] == num:
                    return False
                if board[(row // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == num:
                    return False
            return True

        def find_empty():
            min_options = 10
            best_cell = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        options = sum(is_valid(k, i, j) for k in '123456789')
                        if options < min_options:
                            min_options = options
                            best_cell = (i, j)
            return best_cell

        def solve_sudoku():
            empty = find_empty()
            if not empty:
                return True
            row, col = empty
            for k in '123456789':
                if is_valid(k, row, col):
                    board[row][col] = k
                    if solve_sudoku():
                        return True
                    board[row][col] = '.'
            return False

        solve_sudoku()
```
