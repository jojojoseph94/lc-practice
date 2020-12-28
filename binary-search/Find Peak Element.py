"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
 

Follow up: Could you implement a solution with logarithmic complexity?

Solution : Linear search O(N) time complexity 
           Binary search (O(log(N))) time complexity. Works since no 2 adjacent elements are equal.
           For peak element, calculate mid and see if its greater than element next to it. If yes, prune the right side.
           Otherwise prune the leftside. Finally return the left index.


           Configs possible

           1. 1,2,3,4,5,6
           2. 6,5,4,3,2,1
           3. 1,4,5,6,3,2


"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #brute force
        if len(nums) == 1:
            return 0
        #check if first elem
        if nums[0] > nums[1]:
            return 0
        for i in range(1,len(nums)-1):
            if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
                return i
        #check if last elem
        if nums[-1] > nums[-2]:
            return len(nums)-1
    
    def findPeakElement(self, nums: List[int]) -> int:
        #binary search
        #works only since 2 adjacent elements are not equal
        left = 0
        right = len(nums) - 1
        mid = 0
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left