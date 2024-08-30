# Problem
https://leetcode.com/problems/generate-parentheses/description/

# Intuition
1. Recursive
    - The first thought is to use a backtracking approach to generate all valid combinations of parentheses. By recursively adding ‘(’ and ‘)’ while ensuring the parentheses are well-formed, we can explore all possible combinations.
2. Iterative
   - The iterative approach uses a queue to build the combinations of parentheses. By exploring all possible states iteratively, we can generate all valid combinations without recursion.

# Approach
1. Recursive
    - Use a helper function that takes the current string, the count of left and right parentheses used, and the target number ( n ).
    - If the count of left and right parentheses both reach ( n ), add the current string to the result.
If the count of left parentheses is less than ( n ), add a ‘(’ and recurse.
    - If the count of right parentheses is less than the count of left parentheses, add a ‘)’ and recurse.
    - Use backtracking to explore all possible combinations.
2. Iterative
    - Initialize a queue with an empty string and counts of left and right parentheses.
    - While the queue is not empty, dequeue the front element.
    - If the count of left and right parentheses both reach ( n ), add the current string to the result.
    - If the count of left parentheses is less than ( n ), enqueue the current string with an added ‘(’ and increment the left count.
    - If the count of right parentheses is less than the count of left parentheses, enqueue the current string with an added ‘)’ and increment the right count.
    - Continue this process until all valid combinations are generated.
# Complexity
- Time complexity:
    1. Recursive
        - $$O(4n/squareroot(n​))$$
        - This is derived from the Catalan number, which represents the number of valid parentheses combinations.
    2. Iterative
        - $$O(4n/squareroot(n​))$$
        - Similar to the recursive approach, this is derived from the Catalan number.
- Space complexity:
    1. Recursive
        - The space complexity is determined by the depth of the recursion stack, which can go up to (n).
    2. Iterative
        - $$O(4n/squareroot(n​))$$
        - The space complexity is determined by the number of states stored in the queue, which can be up to the number of valid combinations.
# Code Recursive
```python3 []
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []  # List to store the final valid combinations
        stack = []   # Stack to keep track of the current combination of parentheses

        def backtrack_parathesis_helper(left: int, right: int, n: int, stack: list):
            if left == right == n:  # Base case: if the number of '(' and ')' both reach n
                result.append("".join(stack))  # Add the current combination to the result
                return

            if left < n:  # If the number of '(' is less than n, we can add another '('
                stack.append('(')
                backtrack_parathesis_helper(left + 1, right, n, stack)
                stack.pop()  # Backtrack: remove the last added '('

            if right < left:  # If the number of ')' is less than the number of '(', we can add another ')'
                stack.append(')')
                backtrack_parathesis_helper(left, right + 1, n, stack)
                stack.pop()  # Backtrack: remove the last added ')'

        # Start the backtracking process with 0 '(' and 0 ')' added
        backtrack_parathesis_helper(0, 0, n, stack)
        return result

```
# Code Iterative
```python3 []
from typing import List
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque([("", 0, 0)])  # Initialize the queue with an empty string and counts of left and right parentheses

        while queue:
            current, left, right = queue.popleft()

            if left == right == n:  # If the current combination is valid, add it to the result
                result.append(current)
            if left < n:  # If we can still add a left parenthesis, add it to the queue
                queue.append((current + '(', left + 1, right))
            if right < left:  # If we can still add a right parenthesis, add it to the queue
                queue.append((current + ')', left, right + 1))

        return result
```      
