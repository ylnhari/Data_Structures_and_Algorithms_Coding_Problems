# Problem
https://leetcode.com/problems/permutations-ii/description/
# Intuition
To generate all unique permutations of a list of numbers, we can use a backtracking approach. The main challenge is to handle duplicate numbers and ensure that each permutation is unique. By sorting the list first, we can easily skip over duplicate numbers during the backtracking process.

# Approach
1. **Sort the List**: Start by sorting the list of numbers. This helps in easily identifying and skipping duplicates.
2. **Backtracking**: Use a recursive function to build permutations. At each step, add a number to the current combination and mark it as used.
3. **Skip Duplicates**: If a number is the same as the previous one and the previous one has not been used in the current combination, skip it to avoid duplicate permutations.
4. **Store Results**: When a combination reaches the length of the original list, add it to the result list.
5. **Backtrack**: Remove the last added number and mark it as unused to explore other possibilities.

# Complexity
- Time complexity:
  The time complexity is $$O\left(\frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_m!}\right)$$, where \(n\) is the length of the list and \(k_1, k_2, \ldots, k_m\) are the frequencies of the duplicate elements. This accounts for generating all unique permutations.

- Space complexity:
  The space complexity is $$O(n)$$ for the recursion stack, as the maximum depth of the recursion is \(n\). Additionally, the space required to store the permutations is $$O\left(\frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_m!} \cdot n\right)$$, as each permutation is of length \(n\).

# Code
```python3 []
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = []
        len_nums =  len(nums)
        eligible = [True]*len_nums

        def backtrack(combination: list):

            if len(combination) == len_nums:
                permutations.append(combination[:])
                return

            for i in range(len_nums):
                if eligible[i]:
                    if i > 0 and nums[i] == nums[i-1] and not eligible[i - 1]:
                        continue
                    eligible[i] = False
                    combination.append(nums[i])
                    backtrack(combination)
                    eligible[i] = True
                    combination.pop()

        backtrack([])
        return permutations


                
        
```
