"""
N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?

Leetcode Link : https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class RecursiveSolution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Perform postorder traversal of an n-ary tree recursively.

        Args:
        root (Node): The root of the n-ary tree.

        Returns:
        List[int]: The postorder traversal of the tree's nodes' values.
        """
        post_order_traveral = []

        def search_and_append(node: Node) -> None:
            """
            Helper function to recursively traverse the tree in postorder.

            Args:
            node (Node): The current node being traversed.
            """
            for child_node in node.children:
                search_and_append(child_node)
            post_order_traveral.append(node.val)

        if root:
            search_and_append(root)
        
        return post_order_traveral

class IterativeSolution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Perform postorder traversal of an n-ary tree iteratively.

        Args:
        root (Node): The root of the n-ary tree.

        Returns:
        List[int]: The postorder traversal of the tree's nodes' values.
        """
        if not root:
            return []

        stack1, stack2 = [root], []

        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            for child in node.children:
                stack1.append(child)

        return list(reversed(stack2))

"""
Complexity Analysis
  Recursive Solution:
    Time Complexity: (O(N))
      Each node is visited exactly once.
    Space Complexity: (O(N))
      The space complexity is dominated by the recursion stack. In the worst case (a skewed tree), the recursion stack can go as deep as the number of nodes, (N).
  Iterative Solution:
    Time Complexity: (O(N))
      Each node is visited exactly once.
    Space Complexity: (O(N))
      The space complexity is dominated by the two stacks used. In the worst case, the total space used by both stacks is proportional to the number of nodes, (N).

Advantages and Disadvantages
  Recursive Solution:
    Advantages:
      Simple and easy to understand.
      Naturally follows the postorder traversal logic.
    Disadvantages:
      May lead to a stack overflow for very deep trees due to recursion depth limits.
  Iterative Solution:
    Advantages:
      Avoids potential stack overflow issues by using an explicit stack.
      Can handle very deep trees more robustly.
    Disadvantages:
      Slightly more complex to implement and understand compared to the recursive approach.

Summary
  Both solutions are efficient and valid for postorder traversal of an n-ary tree. The choice between them depends on the specific constraints of your environment, such as recursion depth limits or preference for iterative solutions. The recursive solution is more straightforward, while the iterative solution is more robust for very deep trees.
"""

