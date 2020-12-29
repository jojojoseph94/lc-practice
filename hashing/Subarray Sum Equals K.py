"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

Solution : Bruteforce - for all continuos subarrays, check if sum is equal to target.
            O(N^2) to generate continuos subarrays. sum can be adjusted at each point
            Space complexity : O(1)
            This approach times out.

            Optimized using hashmap - Keep track of running sum.
            Initialize hashmap to {0:1}
             Then check to see if running sum minus k is there in hashmap. If yes, then add the value corresponding to the key 
             to answer.

             Time complexity : O(N)
             Space complexity : O(N)
"""

class Solution:
    def subarraySumBruteForce(self, nums: List[int], k: int) -> int:
        #continuos subarray
        #so 2 loops
        ans = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s+=nums[j]
                if s == k:
                    ans+=1
        return ans
    
    def subarraySumHashmap(self, nums: List[int], k: int) -> int:
        #continuos subarray
        ans = 0
        hm = {0:1}
        s = 0
        for num in nums:
            s+=num
            if s-k in hm:
                #found subarray
                ans+=hm[s-k]
            hm[s] = hm.get(s, 0)+1
        return ans