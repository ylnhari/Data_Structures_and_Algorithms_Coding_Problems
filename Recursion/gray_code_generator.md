# Problem
https://leetcode.com/problems/gray-code/description/

# Intuition
To generate the Gray code sequence, we start with the simplest case (1-bit Gray code) and iteratively build up to the desired number of bits. The key insight is that each additional bit doubles the sequence length, with the new codes being the old codes prefixed by '0' followed by the old codes in reverse order prefixed by '1'.

# Approach
1. **Base Case**: Start with the 1-bit Gray code sequence `['0', '1']`.
2. **Iterative Expansion**: For each additional bit:
   - Prefix '0' to the existing codes.
   - Prefix '1' to the reversed existing codes.
3. **Conversion**: Convert the binary strings to integers for the final result.

# Complexity
- **Time complexity**: The time complexity involves the sum of a geometric progression. For each bit `n`, the number of Gray codes generated is `2^n`. The total number of operations is the sum of this series: $$(2^1 + 2^2 + 2^3 + ... + 2^n)$$ The sum of this geometric series is $$(2 (2^n - 1)$$, which simplifies to $$(O(2^n))$$ for large `n`.
- **Space complexity**: $$O(2^n)$$ because we store all the generated Gray codes.

# Code
```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []

        codes = ['0', '1']
        if n > 1:
            for _ in range(1, n):
                new_codes = ['0' + code for code in codes] + ['1' + code for code in reversed(codes)]
                codes = new_codes

        return [int(code, 2) for code in codes]
