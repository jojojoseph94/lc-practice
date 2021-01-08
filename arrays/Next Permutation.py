"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

Solution : starting from right, find the first decreasing number. If you have a pivot point, now from right find the number greater than pivot. swap these two.
            Once that swap is done, reverse everthing starting from right of pivot.

            Time complexity : O(N)
            Space complexity : O(1)

TODO : This same logic can be applied for strings

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        #find first decreasing from right
        pivot = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        #finding number just larger than pivot to the right
        if pivot >-1:
            swap_pos = len(nums)-1            
            while nums[swap_pos] <= nums[pivot]:
                #print(pivot, swap_pos)
                swap_pos-=1
            swap(pivot, swap_pos)
            
        pivot+=1
        swap_pos = len(nums)-1
        while pivot < swap_pos:
            swap(pivot, swap_pos)
            pivot+=1
            swap_pos-=1