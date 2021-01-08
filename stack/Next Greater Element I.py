"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

Solution : Bruteforce -> For each element in num1, search for it in num2, and then from that index+1 onwards look for a greater element. If found break and add to ans.
            Time complexity : O(M*N) -> M and N are sizes of nums1 and nums2
            Space : O(M) for result

            Optimized -> For each number in nums2, maintain a stack which stores all the numbers greater than itself.
            While maintianing the stack, make sure to add entries in a hashmap for all the popped elements as this element.
            Time complexity : O(M+N) -> For hashmap for the elements in 
            Space : O(M+N) -> For 
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #bruteforce
        ans = []
        for num in nums1:
            flg = False
            d = -1
            for i in range(0,len(nums2)):
                if flg:
                    if nums2[i] > num:
                        d =nums2[i]
                        break
                elif num == nums2[i]:
                    flg = True
            ans.append(d)
        return ans
  
    def nextGreaterElementOptimized(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #optimized
        ans = []
        hm = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                hm[stack.pop()] = num
            stack.append(num)
        while stack:
            hm[stack.pop()] = -1
        for num in nums1:
            ans.append(hm[num])
        return ans
                    