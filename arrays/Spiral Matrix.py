"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100


Solution : Layer by layer. With starting point as 0,0 and ending point as len(matrix)-1, len(matrix[0])-1, print  the outer layer, Then advance starting point and retreat ending point by 1. Do this till they cross.

            Time complexity : O(N), where N is total no of elements. (O(MN) if MN elements)
            Space complexity : O(1)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(i,j,m,n):
            res = []
            for k in range(j,n):
                res.append(matrix[i][k])
            for k in range(i+1,m):
                res.append(matrix[k][n-1])
            if i < m-1 and j < n-1:
                for k in range(n-2,j,-1):
                    res.append(matrix[m-1][k])
                for k in range(m-1,i,-1):
                    res.append(matrix[k][j])
            return res
        
        ans = []
        i = 0
        j = 0
        k = len(matrix)
        l = len(matrix[0])
        while i < k and j < l:
            ans = ans + spiral(i,j,k,l)
            i+=1
            j+=1
            k-=1
            l-=1
        return ans