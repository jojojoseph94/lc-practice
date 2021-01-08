"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = []
Output: 0
Example 3:

Input: costs = [[7,6,2]]
Output: 2
 

Constraints:

costs.length == n
costs[i].length == 3
0 <= n <= 100
1 <= costs[i][j] <= 20

Solution : The cost of painitng a house in a particular color can be stated as
            the minimum cost of painting the previous house in the other colors (NOTE other colors) + cost painting the current 
            house in this color.

            So do this for all colors for all the houses, then return the minimum amount needed to paint the last house.

            Time complexity : O(N)
            Space complexity : O(N) -> O(1) if you modify the input.
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        #paint
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
            
        #print(costs)
        return min(costs[-1])