"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Solution : 1. Using additional O(N) memory and O(N) time complexity. The new index can be found by new_index = (i+k)%len(nums). Copy this to the new array.
              We need this additional memory because we need the original contents for the array while calculating the new indexes.
              If we modify the array as we find indexes, then we would be overwriting and hence answer would be wrong.
Solution 2: O(1) space, O(N) time complexity - 

"""

class Solution:
    def rotateAdditionalMemory(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_arr = [0]*len(nums)
        for i in range(0,len(nums)):
            new_index = (i+k)%len(nums)
            new_arr[new_index] = nums[i]
        for i in range(len(nums)):
            nums[i] = new_arr[i]

    def rotateOptimized(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reversing elements trick
        #reverse the full array
        #then reverse the (n-k) elemets starting from k
        if len(nums) == 1:
            return
        k = k%len(nums)
        nums.reverse()
        for i in range(0,(k//2)):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range(k, k+(len(nums)-k)//2):
            nums[i], nums[k+len(nums)-i-1] = nums[k+len(nums)-i-1], nums[i]