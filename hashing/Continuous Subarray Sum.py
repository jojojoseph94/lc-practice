"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

Solution : Bruteforce -> For all continuos subarrays with size >=2, check if running sum is a multiple of k.
            Time complexity : O(N^2)
            Space complexity : O(1)

            Optimized Hashmap : Keep track of running sum %k in a hashmap. If for any given index, the same runningsum%k occurred previously,
            then that means that the sum of numbers between these 2 indexes is a multiple of k. 
            then just see if the distance between the indexes is atleast 1.

            why add {0:-1} to the hashmap??
            It's because 
            1. we need key 0 to figure out if the running sum is divisible by k.
            2. we need value -1, so that the distance is atleast 2. (If first element itself is a multiple of k, then thats not an answer right)

            Time complexity : O(N)
            Space complexity : O(min(N,k)) -> hashmap min of N and k because we are storing running sum %k only.
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ans = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s+=nums[j]
                if k == 0:
                    if s == 0 and j-i >=1:
                        ans+=1
                else:
                    if s%k == 0 and j-i >=1:
                        ans+=1
        return ans>0

    def checkSubarraySumHashMap(self, nums: List[int], k: int) -> bool:
        #optimized hashmap
        hm = {0:-1}
        s = 0
        for index, num in enumerate(nums):
            s+=num
            if k !=0:
                s%=k
            if s in hm:
                if index - hm[s] > 1:
                    return True
            else:
                hm[s]=index
        return False