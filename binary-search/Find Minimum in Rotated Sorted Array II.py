"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

Solution : Similar to finding the minimum element in rotated sorted array. (variation of binary search)
           with left and right,
           while left < right, keep going to left, if right is bigger than mid. If right is smaller, go to right side.
           If right and mid are same, decrement right
           Time complexity : O(log(N)) most cases -> worst case O(N) (All elements being same)
           Space complexity : O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid+1
            else:
                #mid and right same
                right-=1
        return nums[left]
