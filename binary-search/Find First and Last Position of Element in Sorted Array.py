"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Solution : 2 binary searches; one for left most and one for right most element.
           To find left most element, keep going left until you are less than the element.
           Then check if adjacent element is target. If yes then left_ans is ready. Special case for when left_ans is at beginning.
           Same for right_ans -> Keep going left until you find the target. Check if adjacent one is not target. If yes, then ans.
           Special case for when target at end of array.

           Time complexity : O(log(N))
           Space complexity : O(1)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left_ans = -1
        right_ans = -1
        left=0
        right = len(nums) - 1
        mid = 0
        while left <=right:
            mid = (left+right)//2
            if nums[mid] >= target:
                #if beginning
                if nums[mid] == target and mid == 0:
                    left_ans = 0
                    break
                right = mid-1
            else:
                if mid+1 <len(nums) and nums[mid+1] == target:
                    left_ans = mid+1
                    break
                else:
                    left = mid+1
        if left_ans == -1:
            return [-1, -1]
        left=0
        right = len(nums) - 1
        mid = 0
        while left <=right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid-1
            else:
                if mid+1 <len(nums) and nums[mid] == target and nums[mid+1] != target:
                    right_ans = mid
                    break
                elif mid+1 == len(nums) and nums[mid] == target:
                    #if end case
                    right_ans = mid
                    break
                else:
                    left = mid+1
        return [left_ans, right_ans]