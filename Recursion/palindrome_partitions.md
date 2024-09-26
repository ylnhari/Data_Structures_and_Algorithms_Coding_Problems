# Problem
https://leetcode.com/problems/palindrome-partitioning/description/

# Intuition
The problem requires partitioning a string such that every substring in the partition is a palindrome. A palindrome reads the same forward and backward. The challenge is to explore all possible ways to partition the string and ensure each partitioned substring is a palindrome.

# Approach
We use a backtracking approach to explore all possible partitions of the string. For each starting index, we try to partition the string into all possible substrings and check if each substring is a palindrome. If a substring is a palindrome, we recursively partition the remaining part of the string. We continue this process until we reach the end of the string, at which point we add the current partition to the result list.

# Complexity
- **Time complexity**: The time complexity is $$(O(N \cdot 2^N))$$. This is because there are $$(2^N) $$possible partitions of the string, and for each partition, we may need to check if each substring is a palindrome, which takes$$ (O(N))$$ time.
- **Space complexity**: The space complexity is $$(O(N \cdot 2^N))$$. This includes the space required for the recursion stack and the space needed to store the results.

# Code
```python
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        len_s = len(s)
        result = []
        
        def check_palindrome(inp_str: str) -> bool:
            len_inp_str = len(inp_str)
            for i in range(int(len_inp_str / 2)):
                if inp_str[i] != inp_str[len_inp_str - i - 1]:
                    return False
            return True

        def get_palindrome_partition(index: int, palindrome_list: List[str]):
            if index == len_s:
                result.append(palindrome_list)
                return

            for i in range(index, len_s):
                if check_palindrome(s[index:i + 1]):
                    get_palindrome_partition(i + 1, palindrome_list + [s[index:i + 1]])

        get_palindrome_partition(0, [])
        return result
