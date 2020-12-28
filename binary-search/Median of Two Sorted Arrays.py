"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Solution : Straight fwd -> Merge the two arrays. Return the median of the merged array
           Time complexity : O(N) (To merge the two sorted arrays)
           Space complexity : O(N) for new array

Solution 2 : 

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(N)
        nums3 = []
        l1 = 0
        l2 = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                nums3.append(nums1[l1])
                l1+=1
            else:
                nums3.append(nums2[l2])
                l2+=1
        while l1 < len(nums1):
            nums3.append(nums1[l1])
            l1+=1
        while l2 < len(nums2):
            nums3.append(nums2[l2])
            l2+=1
        if len(nums3)%2:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1]) /2.0

    def findMedianSortedArraysBinarySearch(self, nums1: List[int], nums2: List[int]) -> float:
        #O(log(min(m,n)))
        #TODO