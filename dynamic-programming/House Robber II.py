"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

Solution : Simplify to house robber one. Calculate the answers without the last house and without the first house, separately.
            The max of this will be the answer.

            Time complexity : O(N)
            Space complexity : O(N)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            dp = [0]*len(nums)
            for i in range(0, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        t1 = rob1(nums[:-1])
        t2 = rob1(nums[1:])
        return max(t1, t2)