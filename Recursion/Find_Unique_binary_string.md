
# Problem
https://leetcode.com/problems/find-unique-binary-string/description/

# Intuition
The problem requires finding a binary string of length \( n \) that is different from all the given binary strings in the list `nums`. Since there are \( 2^n \) possible binary strings of length \( n \) and only \( n \) strings in `nums`, there must be at least one binary string that is not in `nums`. The challenge is to generate such a string efficiently.

# Approach
We use a backtracking approach to generate binary strings of length \( n \). Starting with a binary string initialized to all '0's, we recursively flip each bit and check if the resulting string is not in `nums`. If we find a binary string that is not in `nums`, we continue flipping next bit. This recursion ensures we generate all possible binary strings.
# Complexity
- **Time complexity**: The time complexity is $$( O(2^n) )$$ in the worst case, as we may need to explore all possible binary strings of length $$( n )$$.
- **Space complexity**: The space complexity is $$( O(n) )$$ due to the recursion stack and the space required to store the binary string.

# Code
```python
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n = len(nums)
        binary_number = ['0'] * n

        def generate_binary_numbers(index: int):
            if "".join(binary_number) not in nums:
                return "".join(binary_number)

            for i in range(index, n):
                # Flip the current bit
                if binary_number[i] == '0':
                    binary_number[i] = '1'
                else:
                    binary_number[i] = '0'
                
                number = generate_binary_numbers(i + 1)

                if number:
                    return number

        return generate_binary_numbers(0)
