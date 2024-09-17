# Problem 
https://leetcode.com/problems/word-search/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires checking if a given word can be found in a 2D board of characters by moving horizontally or vertically. My first thought is to use a depth-first search (DFS) approach to explore all possible paths in the board starting from each cell. If we find a path that matches the word, we return true.

# Approach
<!-- Describe your approach to solving the problem. -->
1. **Character Count Check**: First, we check if the board contains at least as many of each character as required by the word. If not, we can immediately return false.
2. **Depth-First Search (DFS)**: We use DFS to explore all possible paths in the board. Starting from each cell, we recursively check all four possible directions (up, down, left, right) to see if we can form the word.
3. **Backtracking**: During the DFS, we mark cells as visited by temporarily changing their value. If a path does not lead to a solution, we backtrack by resetting the cell to its original value.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(N \cdot 3^L)$$, where $$N$$ is the number of cells in the board and $$L$$ is the length of the word. In the worst case, we might explore each cell and its three possible directions (excluding the direction we came from) for each character in the word.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $$O(L)$$, where $$L$$ is the length of the word. This is due to the recursion stack used in the DFS.

# Code
```python
from typing import List
from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        total_rows = len(board)
        total_columns = len(board[0])

        if len(word) > total_rows * total_columns:
            return False
        #word pruning is implicitly used in the character 
        #count check before the depth-first search (DFS) begins. This 
        #step ensures that the board contains at least as many of each 
        #character as required by the word. If the board does not have 
        #enough of any character, the function returns False immediately, 
        #avoiding unnecessary computations.
        word_char_count = defaultdict(int)
        for char in word:
            word_char_count[char] += 1
        
        board_char_count = defaultdict(int)
        for row in board:
            for col in row:
                board_char_count[col] += 1
        
        for char, char_count in word_char_count.items():
            if char_count > board_char_count[char]:
                return False

        def search_next_letter(row_index, col_index, word_index):
            if word_index == len(word):  # if word found return True
                return True

            # If search pointer reaches boundaries or cell is already visited, stop searching in that direction
            if row_index >= total_rows or col_index >= total_columns or row_index < 0 or col_index < 0 or board[row_index][col_index] == '*':
                return False

            # don't proceed with searching if the string doesn't match word
            if board[row_index][col_index] != word[word_index]:
                return False

            # Mark the cell as visited
            temp = board[row_index][col_index]
            board[row_index][col_index] = '*'
            word_index += 1

            # Explore all possible directions
            found = (search_next_letter(row_index + 1, col_index, word_index) or
                     search_next_letter(row_index - 1, col_index, word_index) or
                     search_next_letter(row_index, col_index + 1, word_index) or
                     search_next_letter(row_index, col_index - 1, word_index))

            # Reset the cell back to its original value
            board[row_index][col_index] = temp

            return found

        for i in range(total_rows):
            for j in range(total_columns):
                if search_next_letter(i, j, 0):
                    return True

        return False
```
