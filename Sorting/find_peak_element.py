"""Question : https://leetcode.com/problems/find-peak-element/
Final Approach : Find Middle element see if it is a peak else shift to right or left half of the array to find peak in that half.
(if mid is less than its right element then we can atleast find one peak element in the right half of the array similarly 
 if mid is less than its left element then we can atleast find one peak element in the left half of the array)

Thought Process/progression of the Approach
1) Check if first element/last element is peak.
2) else get mid point of the array  and check if its is peak and return.
3) else compare mid with left -> if left > mid -> set end to left
4) else compare mid with right -> if right > mid -> set start to right
5) Repeat steps 2, 3, 4 recursively.
Improvements over original approach
6) Here we can eliminate step 2 as step 3 doesn't satisfy autmatically step 2 satisfies condition
7) we don't need to compare < or > with neighbouring numbers as we proceed because there will always be peak numbers and there are no duplicate neighbours,
   we can just increase or decrease index untill both start and end meet each other.
8) We can eliminate step 1 as those cases are already part of 6 and 7. in that case we can  elimiate step 2 and not step 3 because when there are two elements 
   mid is always the first one (as per our calculation mid/median is left element of two center elements in case of even numbers in an array/sub array).
   So for two elements like [0 , 1] -> if mid is 0 there can be no left lement.
 
Approaches: partition at mid point and checking for peak --> partitions untill both start and end index meet
Time taken: 102 ms                                       --> 53 ms
Memoryused: 14.1 mb                                      --> 13.9 mb
"""
def findPeakElement_1(nums):

    def get_peak_element(nums, start, end):

        piv = start + int((end - start)/2)

        if nums[piv - 1] < nums[piv] > nums[piv + 1]:
            return piv
        elif nums[piv - 1] > nums[piv]:
            end = piv - 1
        elif  nums[piv + 1] > nums[piv]:
            start = piv + 1

        return get_peak_element(nums, start, end)


    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return n - 1
    else:
        return get_peak_element(nums, 0 , n - 1)
      
def findPeakElement_final(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + int((end - start)/2)
        if nums[mid + 1] > nums[mid]:
            start = mid + 1
        else:
            end = mid
    return start
