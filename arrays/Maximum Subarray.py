"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

Solution : Keep running sum, but reset it if you see a larger number. And compare the ans at each point too.

          Time complexity : O(N)
          Space complexity : O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            ans = max(ans, current_sum, num)
            current_sum = max(current_sum, num)
        return ans