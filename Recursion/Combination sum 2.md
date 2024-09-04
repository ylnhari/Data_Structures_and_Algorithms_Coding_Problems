# Problem
https://leetcode.com/problems/combination-sum-ii/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
 To solve the problem of finding all unique combinations in candidates where the candidate numbers sum to target, we can use a backtracking approach. The idea is to explore all possible combinations of the given numbers, ensuring that each combination is unique and sums up to the target value.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Sort the candidates: This helps in easily skipping duplicates and managing the combination generation.
2. Backtracking: Use a recursive function to explore all possible combinations. Start from the current index and explore further by including the current candidate and moving to the next index.
3. Skip duplicates: If the current candidate is the same as the previous one, skip it to avoid duplicate combinations.
4. Base cases: If the sum of the current combination equals the target, add it to the output. If it exceeds the target, stop exploring further.
# Complexity
- Time complexity:
    1. $$O(nlogn+n⋅2n)$$
        
    2. The sorting step takes $$(O(n \log n))$$ and the backtracking step, in the worst case, explores all subsets, which is $$(O(n \cdot 2^n))$$.
- Space complexity:
    1. $$O(n)$$
    2. The space complexity is mainly due to the recursion stack and the space used to store the current combination, which can go up to $$(O(n))$$ in the worst case.
# Code
```python3 []
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates = sorted(candidates)

        def backtrack(combination: list, index: int, sum_c):
            if  sum_c == target:
                output.append(combination.copy())
                return
            elif sum_c > target:
                return
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    combination.append(candidates[i])
                    backtrack(combination, i + 1, sum_c + candidates[i])
                    combination.pop()


        backtrack([], 0, 0)

        return output
      
```
