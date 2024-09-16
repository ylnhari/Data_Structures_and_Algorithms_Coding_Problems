#problem
https://leetcode.com/problems/subsets/description/

# Intuition
To generate all possible subsets of a given list of numbers, we can use a backtracking approach. The idea is to explore all potential combinations by including or excluding each element.

# Approach
We use a recursive function to generate subsets. Starting with an empty subset, we recursively add each element to the current subset and explore further. This ensures that all combinations are considered. The base case is when we've considered all elements, at which point we add the current subset to the list of all subsets.

# Complexity
- Time complexity: 
  The time complexity is $$O(2^n)$$ because each element can either be included or excluded, leading to $$2^n$$ possible subsets.

- Space complexity: 
  The space complexity is also $$O(2^n)$$ to store all the subsets.

# Code
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        all_subsets = []

        def generate_subsets(combination, index):
            all_subsets.append(combination)
            for i in range(index, len_nums):
                generate_subsets(combination + [nums[i]], i + 1)
        
        generate_subsets([], 0)
        return all_subsets
