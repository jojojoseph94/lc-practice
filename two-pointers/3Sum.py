"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Solution : Sort the numbers. Then iterate over numbers till 0 to search for the complement of it in the right side of the array.
            2 sum is done using a set, storing the seen numbers at each point.

            Time complexity : O(N^2)
            Space complexity : O(N)

        Solution 2 : Nosort : O(N^2), but keep track of duplicates in a set so that duplicates are not added to the answer.
            Time complexity : O(N^2)
            Space complexity : O(N)
TODO what about other methods ?? No sort and all
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, i, ans):
            seen = set()
            j = i+1
            while j < len(nums):
                complement = -nums[i]-nums[j]
                if complement in seen:
                    ans.append([nums[i], complement, nums[j]])
                    while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j+=1
                seen.add(nums[j])
                j+=1
                
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                twoSum(nums, i, ans)
        return ans

    def threeSumNoSort(self, nums: List[int]) -> List[List[int]]:
        duplicates = set()
        ans = set()
        seen = {}
        #not resetting k is an optimization 
        #other option is to clear the seen every time
        #you are done with an i
        for i in range(0,len(nums)):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
                for j in range(i+1, len(nums)):
                    complement = -nums[i]-nums[j]
                    if complement in seen and seen[complement] == i:
                        ans.add(tuple(sorted([nums[i], nums[j], complement])))
                    seen[nums[j]] = i
        return ans