"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

Solution : 1. Linear kind of search but clever using 2 pointers. O(M+N)

           2. Binary search - Think of the 2D array as a 1D array with MN elements. Then the index of MN element can be written 
           as arr[MN//N][MN%N] -> Use this for binary search.
           
           Time complexity : O(log(MN))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #linear search O(M+N)
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i+=1
            else:
                j-=1
        return False
    
    def searchMatrixBinary(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m*n) -1
        while left <= right:
            mid = (left+right)//2
            mid_ele = matrix[mid//n][mid%n]
            if mid_ele == target:
                return True
            else:
                if target < mid_ele:
                    right = mid-1
                else:
                    left = mid+1
        return False