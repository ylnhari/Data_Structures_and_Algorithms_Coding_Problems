# problem
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Intuition
- Recursive Approach: The postorder traversal of an n-ary tree involves visiting the children of a node before visiting the node itself. This naturally lends itself to a recursive solution.
- Iterative Approach: An iterative solution can be achieved using a stack to simulate the recursive calls. We push the root node onto the stack and then repeatedly pop nodes and push their children onto the stack until the stack is empty.

# Approach
- Recursive Approach:
    1. If the root node is None, return an empty list.
    2. Create an empty list to store the postorder traversal.
    3. Recursively traverse each child node.
    4. Append the current node's value to the list.
    5. Return the list.
    
- Iterative Approach:
    1. If the root node is None, return an empty list.
    2. Initialize two stacks: one for storing nodes and the other for
    3. storing values.
    4. Push the root node onto the first stack.
    5. While the first stack is not empty:
    6. Pop a node from the first stack.
    7. Push the node's value onto the second stack.
    8. Push the node's children onto the first stack in reverse order (to simulate left-to-right traversal).
    9. Reverse the second stack and return it.

# Complexity
- Time complexity:
    - Recursive Approach: O(N) where N is the number of nodes. Each node is visited exactly once.
    - Iterative Approach: O(N) for the same reason.


- Space complexity:
    - Recursive Approach: O(H) where H is the height of the tree. This is due to the recursion stack.
    - Iterative Approach: O(N) in the worst case (a skewed tree) where the maximum number of nodes can be on a single path.
# Recursive solution
```python3 []
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

```

# Iterative solution
```python3 []
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

```

# Advantages and Disadvantages
- Recursive Solution:
    - Advantages:
      - Simple and easy to understand.
      - Naturally follows the postorder traversal logic.
    - Disadvantages:
      - May lead to a stack overflow for very deep trees due to - - recursion depth limits.
- Iterative Solution:
    - Advantages:
      - Avoids potential stack overflow issues by using an explicit stack.
      - Can handle very deep trees more robustly.
    - Disadvantages:
      - Slightly more complex to implement and understand compared to the recursive approach.

# Summary
- Both solutions are efficient and valid for postorder traversal of an n-ary tree. The choice between them depends on the specific constraints of your environment, such as recursion depth limits or preference for iterative solutions. The recursive solution is more straightforward, while the iterative solution is more robust for very deep trees.
