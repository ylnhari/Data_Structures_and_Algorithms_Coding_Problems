# Problem
https://leetcode.com/problems/combinations/description/
# Intuition
To generate all possible combinations of `k` numbers out of `n`, we can use a backtracking approach. The idea is to build combinations incrementally and backtrack when a combination reaches the desired length.

# Approach
We use a recursive function to explore all possible combinations. Starting from an empty combination, we add elements one by one. If a combination reaches the length `k`, we add it to the result list. We then backtrack by removing the last added element and continue exploring other possibilities.

# Complexity
- Time complexity: 
  The time complexity is $$O(C(n, k) * k)$$, where $$C(n, k)$$ is the number of combinations, given by the binomial coefficient $$\frac{n!}{k!(n-k)!}$$. Each combination requires operations proportional to `k`.

- Space complexity:
  The space complexity is $$O(k)$$ for the recursion stack, as the maximum depth of the recursion is `k`. Additionally, the space required to store the result is $$O(C(n, k) * k)$$.

# Code
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def backtrack_combinations_k(combination, index):
            if len(combination) == k:
                answer.append(combination[:])
                return
            remaining_values = k - len(combination)
            max_value_to_search = n - remaining_values
            # +2 because -> +1 since range excludes last and another +1 since we are starting the index at 1
            for i in range(index, max_value_to_search + 2): 
                combination.append(i)
                backtrack_combinations_k(combination, i + 1)
                combination.pop()

        backtrack_combinations_k([], 1)
        return answer
