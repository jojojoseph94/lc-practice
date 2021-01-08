"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

Solution : Bruteforce - for each index, height find the max elements at both left and right side. Then the water which can be fit on top
            of the corresponding index is, the difference minimum of max elements from left and right and the height. (If positive add to answer)
            Time complexity : O(N^2)
            Space : O(1)

            Optimized : No need to recalculate the left and right maxes at each point every time. Just do it once and save it in an array.
            This brings down the time complexity to O(N)
            But we will also use space O(N)

            TODO : O(1) space 2 pointer method
"""

class Solution:
    def trapBrute(self, height: List[int]) -> int:
        ans = 0
        for i in range(0,len(height)):
            #find how much water can fit on top of this
            left_max = 0
            right_max = 0
            for j in range(0,i):
                left_max = max(left_max, height[j])
            for j in range(i+1,len(height)):
                right_max = max(right_max, height[j])
            #print(i, height[i], left_max, right_max, min(left_max, right_max) - height[i])
            if min(left_max, right_max) - height[i] > 0:
                ans+=(min(left_max, right_max) - height[i])
        return ans

    class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        lefts = [0]*len(height)
        rights = [0]*len(height)
        for i in range(1,len(height)):
            lefts[i] = max(lefts[i-1], height[i-1])
            rights[len(height)-i-1] = max(rights[len(height)-i], height[len(height)-i])
        for i in range(0,len(height)):
            if min(lefts[i], rights[i]) > height[i]:
                ans+=(min(lefts[i], rights[i]) - height[i])
        return ans
            