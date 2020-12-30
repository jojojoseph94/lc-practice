"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Solution 1 : Counting sort - 2 pass
             Count the number of occurances of each of these colors and then replace the array
             Time complexity : O(N) 2 pass
             Space complexity : O(1)

Solution 2 : 2 pointer single pass. 
             Here keep 3 pointers, one for red, white and blue.Assume red and white starts at 0 and blue at the end.
             Then while white <=blue, see if the current element at white pointer is at correct position.
             If it isn't exchange with red or blue pointers and advance the pointers. (Don't advance the white pointer 
             if u swapped with an element in the right)
             Time complexity : O(N)
             Space complexity : O(1)
             
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_r = 0
        num_w = 0
        num_b = 0
        for num in nums:
            if num == 0:
                num_r+=1
            elif num == 1:
                num_w +=1
            else:
                num_b+=1
        #print(0, num_r+1, num_r+num_w)
        print(num_r, num_r + len(nums)-num_r-num_b, len(nums)-num_b)
        for i in range(0,num_r):
            nums[i] = 0
        for i in range(num_r,num_r + len(nums)-num_r-num_b):
            nums[i] = 1
        for i in range(num_r+num_w,len(nums)):
            nums[i] = 2

    def sortColorsOnePass(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red+=1
                white+=1
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue-=1
            else:
                white+=1