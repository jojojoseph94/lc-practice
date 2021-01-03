"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Solution : Mark negative -> Time complexity O(N), Space complexity : O(1)
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #mark negative
        res = []
        for i in range(0,len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] *=-1
        for i in range(1,len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
        return res
