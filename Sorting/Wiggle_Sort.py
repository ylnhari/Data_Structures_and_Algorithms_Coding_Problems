"""Question : Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3] so on

Constraints:
1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000

Thought Process/progression of the Approach 
1) sort the array.
2) divide array in half at mid point (median) into two arrays containing smaller_elements, larger_elements.
3) Reverse both the arrays so that the chances of duplicates being adjacent(median element being duplicate is the main problem here) to each other reduces.
4) Then Merge those arrays into one by replacing -> odd indexed places in the array with smaller_elements array and even indexed places in the array with 
larger_elements array.
"""

def wiggleSort(array) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  
  # This approach is clearly explained by Mr. steffanPochmann Here -> https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
  array.sort() # o(nlogn)
  length = len(array)

  median = len(array[::2]) - 1

  odds = array[median::-1]
  even = array[:median:-1]

  array[::2], arrays[1::2] = odds, even
