"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

Solution : Bruteforce -. Look to the right. If not look from front
            Time complexity : O(N^2)
            Space complexity : O(N) - for results

            Solution 2 - Create a stack and hm. Stack stores the indexes for which we are not able to find a greater number
            to the right and hm stores the indexes along with their greater numbers to the right. Keep track of the max element 
            also since that can be set in hm to -1 at the end.

            Then iterate over the array indices looking to see if you have an entry in the HM.If it is their add to answer.
            If not then start from beginning to check. This can result in O(N^2) if the sequence is decreasing in nature.
            Time complexity : O(N^2)
            Space complexity : O(N)

            Solution 3 : Maintain a stack which contains indexes greter than the current element only.
                         So when you pop elements from the stack, you know that these are the indexes which have nums[i] as the answer.

                         Do this twice and you get answer for circular array.

                         https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice

            Time complexity : O(N)
            Space complexity : O(N)

"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        #bruteforce
        for i in range(0,len(nums)):
            flg = False
            d = -1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    d = nums[j]
                    flg = True
                    break
            #check front
            if not flg:
                for j in range(0, i):
                    if nums[i] < nums[j]:
                        d = nums[j]
                        break
            ans.append(d)
        return ans

    def nextGreaterElementsSolution2(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        hm = {}
        if not nums:
            return ans
        mx = nums[0]
        mx_index = 0
        for index, num in enumerate(nums):
            #print(hm, stack)
            while stack and nums[stack[-1]] < num:
                hm[stack.pop()] = num                
            stack.append(index)
            if mx < num:
                mx = max(mx, num)
                mx_index = index
        hm[mx_index] = -1
        for i in range(0,len(nums)):
            if i in hm:
                ans.append(hm[i])
            else:
                #check from first?
                d = -1
                for j in range(0,i):
                    if nums[j] > nums[i]:
                        d = j
                        break
                if d >=0:
                    ans.append(nums[d])
                else:
                    ans.append(d)
        return ans

    def nextGreaterElements3(self, nums: List[int]) -> List[int]:
        #stack optimized
        ans = [-1]*len(nums)
        stack = []
        for i in range(2*len(nums)):
            i = i%len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return ans