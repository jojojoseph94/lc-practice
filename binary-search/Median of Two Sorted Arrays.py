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

Solution 2 : For binary search approach, we are trying to find the mid element of the combined array.
             For this we first find the smaller length array.
             Then for the combined arrays, we need to find the mid point so that we have
             l1, l2, r1, r2
             elements where l1 and r1 belong to the first array and l2 and r2 belong to the second array.
             If we have partx elements from the first array, then the second array will have (N+M+1)//2 - partx
             elements. (Why - cause partx + party will give you the mid point of the combined arrays).
             Now our objective is to move the partx to the right or paty to the left.
             You can do that by checking if l1 > r2 or l2 > r1.
             You can 1. move partx to the right if l2 > r1
                     2. move party to the left if l1 > r2

            Time complexity : O(log(min(M, N)))
            Space complexity : O(1)

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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        low = 0
        high = n
        while low <= high:
            partx = (low + high)//2
            party = (n+m+1)//2 - partx
            l1 = float('-inf') if partx-1 < 0 else nums1[partx-1]
            l2 = float('-inf') if party-1 < 0 else nums2[party-1]
            r1 = float('inf') if partx >= n else nums1[partx]
            r2 = float('inf') if party >=m else nums2[party]
            #print(partx, l1, r1, party, l2, r2)
            if l1 > r2:
                high = partx-1
            elif l2 > r1:
                low = partx+1
            else:
                if (m+n)%2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2.0
                else:
                    return max(l1,l2)
        return -1