"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

Solution : 1. Backtracking solution - find the perimter and value of one side in the square. Now for the sqaure, keep building the sides, so long as it doesn't exceed the one side length.
                                      Once you are done with all the sticks, check to see if all the sides are the same.
              Time complexity : You try all 4 sides and for each side of square, so the comibations can be in worst case
                                4^n
              Space complexity : O(N) 

            2. DP solution -> TODO
"""

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        #backtrack
        self.ans = False
        if not nums:
            return False
        nums = sorted(nums, reverse=True)
        perimeter = sum(nums)
        self.one_side = perimeter//4
        if self.one_side*4 != perimeter:
            return False
        
        def backtrack(side1, side2, side3, side4, cur):
            if cur >= len(nums):
                if side1 == side2 == side3 == side4:
                    self.ans = True
                    return
            else:
                if not self.ans and side1+nums[cur] <= self.one_side:
                    backtrack(side1+nums[cur], side2, side3, side4, cur+1)
                if not self.ans and side2+nums[cur] <= self.one_side:
                    backtrack(side1, side2+nums[cur], side3, side4, cur+1)
                if not self.ans and side3+nums[cur] <= self.one_side:
                    backtrack(side1, side2, side3+nums[cur], side4, cur+1)
                if not self.ans and side4+nums[cur] <= self.one_side:
                    backtrack(side1, side2, side3, side4+nums[cur], cur+1)    
        backtrack(nums[0], 0, 0, 0, 1)
        return self.ans