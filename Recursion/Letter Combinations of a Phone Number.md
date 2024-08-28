# problem
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Intuition
- Recursive Backtracking
    - The first thought is to use a recursive approach to explore all possible combinations. Backtracking is a natural fit for this problem because it allows us to build combinations incrementally and backtrack when we reach an invalid state.
- Iterative Backtracking
    - An iterative approach can be used to build combinations step-by-step without recursion. This can be more intuitive for some and avoids the overhead of recursive calls.

# Approach
- Recursive Backtracking
    - Create a mapping of digits to their corresponding letters.
    - Use a recursive function to build combinations:
        1. If the current combination length equals the length of the input digits, add it to the result list
        2. Otherwise, for each letter corresponding to the current digit, append the letter to the current combination and recursively build the next part of the combination.
    - Start the recursion with an empty combination and the first digit.
- Iterative Backtracking
    - Create a mapping of digits to their corresponding letters.
    - Initialize a list with an empty string to start building combinations.
    - For each digit in the input:
        1. Create a temporary list to store new combinations.
        2. For each existing combination, append each letter corresponding to the current digit and add the new combination to the temporary list.
        3. Update the result list with the new combinations.
    - Return the result list containing all possible combinations.

# Complexity
- Time complexity:
    - Recursive Backtracking
        - $$O(4^n)$$
        - where ( n ) is the length of the input digits. Each digit can map to up to 4 letters, leading to ( $$4^n$$ ) possible combinations in the worst case.
    - Iterative Backtracking
        - $$O(4^n)$$
        - where ( n ) is the length of the input digits. Similar to the backtracking approach, each digit can map to up to 4 letters, leading to ( $$4^n$$ ) possible combinations in the worst case.
    

- Space complexity:
    - Recursive Backtracking
        - $$O(4^n)$$
        - where ( n ) is the length of the input digits. This accounts for the recursion stack depth.
    - Iterative Backtracking
        - $$O(4^n)$$
        - where ( n ) is the length of the input digits. This accounts for storing all possible combinations.

# Code recursive
```python3 []
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2' : 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        output = []

        if digits == '':
            return output

        l_d = len(digits)
        def back_trace(index: int, combination: List):
            if len(combination)  == l_d:
                output.append("".join(combination))
                return
            mapping_string = mapping[digits[index]]
            for letter in mapping_string:
                combination.append(letter)
                back_trace(index + 1, combination)
                combination.pop()

        
        back_trace(0, [])

        return output
```

# Code iterative
```python3 []
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = ['']
        for digit in digits:
            temp = []
            for combination in result: ''
                for letter in mapping[digit]: #abc
                    temp.append(combination + letter)
            result = temp

        return result
```        
