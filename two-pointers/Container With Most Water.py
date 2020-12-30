"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


Solution : 2 pointers -> left at zero and right at end. At each point calculate the water which can be filled.
                         Then move left or right based on whichever value is smaller. (Why? Because we already calculated the
                         max possible value for this combo. Now no point in using the same small height)

            Time complexity : O(N)
            Space complexity : O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while left <right:
            h1 = height[left]
            h2 = height[right]
            h = min(h1, h2)
            water = (right - left)*h
            ans = max(ans, water)
            if h == h1:
                left+=1
            else:
                right-=1
        return ans