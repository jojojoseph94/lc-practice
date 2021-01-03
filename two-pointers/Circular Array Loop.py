"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
 

Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000
 

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?

Solution 1 : O(N^2) complexity - 2 pointers
                            slow and fast pointers which jump once or twice. But keep track of direction and length of the loop.
                            Set slow and fast at all possible locations.
Solution 2 : O(N) complexity : For every position, process it, then unset it so that it wont be processed again.
                               Process implies while you can jump and direction is same as how you started and you are not a single jump
                               loop, jump to next position and continue jumping if you can.
                               After processing each element, see if you reached back at the beginning. If yes, u have a loop.
                            
"""



def circularArrayLoopOptimized(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            mark = str(i)
            direction = nums[i]
            #type direction and single jump
            while type(nums[i]) == int and direction*nums[i] > 0 and nums[i]%len(nums)!=0:
                jump = nums[i]
                nums[i] = mark
                i = (i + jump)%len(nums)
            if nums[i] == mark:
                return True
        return False

class Solution:
    def circularArrayLoopTwoPointer(self, nums: List[int]) -> bool:
        if not nums:
            return False
        def move(index):
            return (index+nums[index])%len(nums)
        
        for k in range(0,len(nums)):
            slow = k
            direction = nums[k]
            fast = move(slow)
            if direction*nums[fast] <0:
                continue
            if direction*nums[slow] <0:
                continue
            fast = move(fast)
            if direction*nums[fast] <0:
                continue
            while 1:
                if slow == fast:
                    if move(slow) == slow:
                        break
                    else:
                        return True
                slow = move(slow)
                #check direction change
                if direction*nums[slow] <0:
                    break
                fast = move(fast)
                if direction*nums[fast] <0:
                    break
                fast = move(fast)
                if direction*nums[fast] <0:
                    break
        return False