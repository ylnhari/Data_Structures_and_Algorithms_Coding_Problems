# Problem
https://leetcode.com/problems/binary-tree-paths/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires finding all root-to-leaf paths in a binary tree. My initial thought is to use a depth-first search (DFS) approach to traverse the tree. As we traverse, we can build the path string and add it to the result list when we reach a leaf node.

# Approach
<!-- Describe your approach to solving the problem. -->
1. **Depth-First Search (DFS)**: Use a recursive DFS approach to traverse the tree.
2. **Path Construction**: As we traverse, we build the path string by appending the current node's value.
3. **Leaf Node Check**: When we reach a leaf node (a node with no left or right children), we add the constructed path to the result list.
4. **Edge Case**: If the root is `None`, return an empty list.

# Complexity
- Time complexity: 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$, where \( n \) is the number of nodes in the tree. We visit each node exactly once.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$, where \( n \) is the number of nodes in the tree. This is due to the recursion stack in the worst case (a completely unbalanced tree).

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []

        def traverse_binary_tree(node, current_path: str):
            if node:
                current_path += str(node.val)
                if not node.left and not node.right:  # If it's a leaf node
                    paths.append(current_path)  # Append the path to paths
                else:
                    current_path += '->'  # Add the arrow for the next node
                    traverse_binary_tree(node.left, current_path)
                    traverse_binary_tree(node.right, current_path)

        traverse_binary_tree(root, "")
        return paths
