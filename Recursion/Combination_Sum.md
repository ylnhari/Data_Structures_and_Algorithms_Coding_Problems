# Problem
https://leetcode.com/problems/combination-sum/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem is to find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may be used an unlimited number of times. My first thought is to use a recursive approach to explore all possible combinations.

# Approach
<!-- Describe your approach to solving the problem. -->
1. **Filter and Sort Candidates**: First, filter out candidates greater than the target and sort the remaining candidates.
2. **Recursive Function**: Use a recursive function to explore all combinations. The function will:
   - Check if the current combination sums to the target. If it does, add it to the result list.
   - If the sum is less than the target, recursively add each candidate to the current combination and continue the search.
3. **Avoid Duplicates**: Ensure that each combination is unique by maintaining the order of candidates.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(2^n)$$ in the worst case, where \( n \) is the number of candidates. This is because each candidate can either be included or excluded from a combination.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $$O(n)$$ due to the recursion stack and the space required to store the combinations.

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may be used an unlimited number of times.

        :param candidates: List of candidate numbers.
        :param target: Target sum for the combinations.
        :return: List of lists, where each list is a unique combination of numbers that sum to target.
        """
        
        # Filter out candidates greater than the target and sort the remaining candidates
        candidates = [i for i in candidates if i <= target]
        candidates = sorted(candidates)
        num_candidates = len(candidates)
        combinations = []

        def check_recursively(combination: list, candidate_index: int):
            """
            Recursively explores all combinations of candidates that sum to the target.
            
            :param combination: Current combination of numbers being explored.
            :param candidate_index: Current index in the candidates list.
            :return: True if a valid combination is found, False otherwise.
            """
            
            sum_c = sum(combination)
            
            # Base case: if the current combination sums to the target, add it to the results
            if sum_c == target:
                combinations.append(combination)
                return True

            # If the current sum is less than the target, continue exploring
            elif sum_c < target:
                for i in range(candidate_index, num_candidates):
                    next_value = candidates[i]
                    
                    # If the next candidate exceeds the target, break the loop
                    if next_value > target:
                        break
                    
                    # Recursively add the next candidate to the current combination
                    elif check_recursively(combination + [next_value], candidate_index):
                        pass
                    else:
                        candidate_index += 1
                
                return False

        # Start the recursive exploration with an empty combination and the first candidate index
        check_recursively([], 0)
        return combinations

