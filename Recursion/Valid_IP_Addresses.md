# Problem
https://leetcode.com/problems/restore-ip-addresses/description/

# Intuition
The problem requires generating all possible valid IP addresses from a given string. An IP address consists of four blocks separated by dots, and each block is a number between 0 and 255. The challenge is to split the string into these blocks while ensuring each block is valid.

# Approach
We use a backtracking approach to explore all possible ways to split the string into four valid blocks. We recursively build the IP address by adding one block at a time and checking its validity. If a block is valid, we proceed to the next block; otherwise, we backtrack and try a different split.

# Complexity
- **Time complexity:** The time complexity is $$O(3^4)$$ because each block can have at most 3 digits, and there are 4 blocks.
- **Space complexity:** The space complexity is $$O(n)$$ due to the recursion stack and the space required to store the resulting IP addresses.

# Code
```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        len_s = len(s)
        ips = []

        def search_ipaddresses(index, ip_addr, block_number):
            # If we have reached the end of the string and have exactly 4 blocks, add the IP address to the list
            if index == len_s and block_number == 4:
                ips.append(ip_addr)
                return

            remain_blocks = 4 - block_number
            min_chars, max_chars = remain_blocks * 1, remain_blocks * 3

            # Check if the remaining characters can form valid blocks
            if not (min_chars <= (len_s - index) <= max_chars):
                return

            for i in range(index, len_s):
                # Do not try to find IP addresses with block length > 3
                if (i - index) >= 3:
                    break

                # Skip blocks that start with '0' but are longer than 1 character
                if s[index] == '0' and (i - index) > 0:
                    break

                # Skip blocks that are greater than 255
                if (i - index) == 2 and int(s[index: i + 1]) > 255:
                    break

                # If this is the last block, do not add a dot
                if block_number + 1 == 4:
                    search_ipaddresses(i + 1, ip_addr + s[index: i + 1], block_number + 1)
                else:
                    search_ipaddresses(i + 1, ip_addr + s[index: i + 1] + '.', block_number + 1)

        search_ipaddresses(0, '', 0)

        return ips
