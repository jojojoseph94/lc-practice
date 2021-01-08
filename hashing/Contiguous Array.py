"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

Solution : Bruteforce - Iterate over all subarrays, keeping track of the number of zeros and ones. If they are equal, 
                        Check to see if the length of the subarray is greater than the already stored answer
            Time complexity : O(N^2)
            Space complexity : O(1)
            
            Optimized Hashmap - So keep track of the number of 1's ans 0's using a variable which is incremented / decremented based on
            1 or 0. If this variable is zero, it means you have a candidate array.
            Keep the count while iterating over the array, checking to see if you have seen the same number of 1's and 0's before.
            If you have seen the same number of one's and zero's then that means between the old index of the count and the new one, you 
            have a candidate subarray. Update the hashmap only if the count is not seen (As you are going for longest subarray, you dont wanna
            overwrite the old indexes)

            Time complexity : O(N)
            Space complexity : O(N)
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,len(nums)):
            n_zero = 0
            n_one = 0
            for j in range(i, len(nums)):
                if nums[j]:
                    n_one+=1
                else:
                    n_zero+=1
                if n_zero == n_one:
                    ans=max(ans, j-i+1)
        return ans

    def findMaxLengthHashMap(self, nums: List[int]) -> int:
        hm = {0:-1}
        count = 0
        ans = 0
        for i in range(0,len(nums)):
            if nums[i]:
                count+=1
            else:
                count-=1
            if count in hm:
                ans = max(ans, i-hm[count])
            else:
                hm[count] = i
        return ans