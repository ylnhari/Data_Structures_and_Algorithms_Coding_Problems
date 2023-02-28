# Problem Statement
https://leetcode.com/problems/add-two-numbers/
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Let's try a simple Method, get the numbers value from each linked list and add them and from the addition result create a new linked list.If we could calculate the number value while etracting each digit from the linked list we could save some space.
# Approach
<!-- Describe your approach to solving the problem. -->
1. first go through each linked list and calculate the value on the go, for example for linked list -> **4-9-1 => our for loop will calulate the value of the number as  4 * 1 (1 st loop) + 9 * 10 (2 nd loop) + 1 * 100 (3 rd loop)** , so value of number in linked list is 194.Below Function is used to calculate number value as described above.

```python []
def extract_number_from_linked_list(node:  Optional[ListNode]):
        position_value = 1
        number_value = node.val * position_value 
        while node.next:
            node = node.next
            position_value = position_value * 10
            number_value += node.val*position_value
        return number_value
```
2. Once you have both numbers, add them and convert the result into string.

```python []
added_value = extract_number_from_linked_list(l1) + extract_number_from_linked_list(l2)
```

3. Now using each character(actually digit) in the string create a Linked List and return it.
```python []
next_node_reference = None
for digit in str(added_value):
    digit_node = ListNode(digit)
    digit_node.next = next_node_reference
    next_node_reference = digit_node
```
# Complexity
- **Time complexity**: Since we go through each digit in the list and perform the addition
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
 $$O(n)$$
- **Space complexity**: Since we need create and store result linked list and result itself whose length would be approximately the lenth of largest of two input linked list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
 $$O(n)$$
# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        def extract_number_from_linked_list(node:  Optional[ListNode]):
            position_value = 1
            number_value = node.val * position_value 
            while node.next:
                node = node.next
                position_value = position_value * 10
                number_value += node.val*position_value
            return number_value

        added_value = extract_number_from_linked_list(l1) + extract_number_from_linked_list(l2)

        next_node_reference = None
        for digit in str(added_value):
            digit_node = ListNode(digit)
            digit_node.next = next_node_reference
            next_node_reference = digit_node

        return digit_node

```
