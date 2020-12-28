"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

The Binary search part is a followup ofg this question -> This question is very open ended.

Solution 1: Here duplicates are ignored. So we can use a set to store result.
            Create a hashmap/counter of the larger list. Then for each element in the smaller list, check if it is there in the counter/hashmap, if yes add it to the answer.

            Time complexity : O(N) -> If the larger list is huge and small list is very small, then this is not ideal.
            Space complexity : O(N) -> hashmap with all unique items can be a prob;lem

This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.
Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken into consideration). You are told the lists are sorted.

Cases to take into consideration include:
duplicates, negative values, single value lists, 0's, and empty list arguments.
Other considerations might include
sparse arrays.

Solution : If the lists are sorted, maybe we can apply binary search to find the left and right boundaries of the intersection. Then we can perform the following intersection but with a smaller subset of the larger array?(Solution2)

Follow-ups
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #computing intersection
        #duplicates -> ignore; so using set
        ans = set()
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        hm = Counter(nums1)
        for num in nums2:
            if num in hm:
                ans.add(num)
        return ans

    def intersectSortedBinary(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        left = 0
        right = len(nums1)-1
        while left < right:
            mid = (left+right)//2
            if nums1[mid] >= nums2[0]:
                right = mid
            else:
                left = mid+1
        left_start = left
        left = 0
        right = len(nums1)-1
        while left < right:
            mid = (left+right)//2
            if nums1[mid] <= nums2[-1]:
                left = mid+1
            else:
                right = mid
        right_start = left
        cur = 0
        #2 pointers
        ans = []
        while left_start <= right_start and cur < len(nums2):
            if nums2[cur] == nums1[left_start]:
                ans.append(nums2[cur])
                cur+=1
                left_start+=1
            elif nums2[cur] < nums1[left_start]:
                cur+=1
            else:
                left_start+=1
        return ans