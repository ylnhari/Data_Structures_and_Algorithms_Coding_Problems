"""Question : Question : https://leetcode.com/problems/find-peak-element/
Final Approach : count coulour 0, 1, 2 and loop through counts to generate final array

Thought Process/progression of the Approach
1) get counts of colours in new array.
2) loop through counts array , nested loop from 0 to current element of count array-> replace current pointer element of input array with index of count array , increase pointer by 1
 
Approaches: count sort
Time taken: 46 ms
Memoryused: 13.8
"""
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    counts = [0]*3
    for i in nums:
        counts[i]+=1

    k = 0
    for j in range(0,len(counts)):
        for i in range(0, counts[j]):
            nums[k] = j
            k+=1
