"""
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

 

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
The length of the array will be in the range [1, 10^4].

Solution : Since we cannot apply normal binary search as we don't know where the search boudary is, start with roght = 1 and try to find the right boundary by changing
            right to right * 10 and left to right every time you are not within the target boundary.

            Once in the target boundary, you can perform normal binary search.
            Time complexity : O(log(N))
            Space complexity : O(1)
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right *= 10
        while left <= right:
            mid = (left + right) //2
            num = reader.get(mid)
            if num == target:
                return mid
            elif target < num:
                right = mid - 1
            else:
                left = mid + 1
        return -1