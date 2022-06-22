"""Final Approach : Randomized Quick sort restricted to sort only those partitions of original array that has the Kth Largest  element

Thought Process/progression of the Approach 

1) sort the array , get the K th largest in Sorted array.
2) which sort to use -> i picked quick sort but worst case scenario Time Complexity for quick sort is O(n2)
3) Randomize pivot selection -> then quick sort worst case scenario Time Complexity reduces to O(nlogn)
4) Instead of sorting whole array , sort only those partitions that has K largest element.


Approaches: quick sort --> randomized quick sort --> restricting the sort to right partitions
Time taken: 5771 ms    --> 209 ms                --> 102 ms
Memoryused: 20.3 mb    --> 14.9 mb               --> 14.8 mb


Question : find kth largest element in an array `nums`
constraints : 1 <= k <= 10**4
              -10**4 <= nums[i] <= 10**4
"""
from random import randint

def findKthLargest(nums, k):

    def partition(array, pivot_index, len_of_the_array):
        """
            Partition the array into two parts where left part has numbers
            always < pivot and all the other numbers are on right partition
            with the center element for these partitions being the pivot element.
        """
        pivot = array[pivot_index]
        swap_index = pivot_index
        for compare_index in range(pivot_index+1, len_of_the_array+1):
            if array[compare_index] < pivot:
                swap_index+=1
                array[swap_index], array[compare_index] = array[compare_index], array[swap_index]

        array[pivot_index], array[swap_index] = array[swap_index], array[pivot_index]

        return swap_index

    def quick_sort(array, pivot_index, len_of_the_array, kth_largest_element_index):
        """
            A recursive quick sort function using randomized pivot selection.
        """
        if pivot_index < len_of_the_array:
            new_pivot_index = randint(pivot_index, len_of_the_array)
            # using randomized quick sort
            array[pivot_index], array[new_pivot_index] = array[new_pivot_index], array[pivot_index]
            # recursion part of quick sort
            pivot_index_after_partition = partition(array, pivot_index, len_of_the_array)

            # restricting sorting to only the partitions should have the Kth Highest Element
            if pivot_index_after_partition == kth_largest_element_index:
                return
            elif pivot_index_after_partition > kth_largest_element_index:
                quick_sort(array, pivot_index, pivot_index_after_partition - 1, kth_largest_element_index)
            else:
                quick_sort(array, pivot_index_after_partition + 1, len_of_the_array, kth_largest_element_index)

array = nums
kth_largest_element_index = len(nums) - k
quick_sort(array, 0, len(nums) - 1, kth_largest_element_index)

return array[kth_largest_element_index]
