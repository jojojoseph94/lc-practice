"""
Solution : starting from right, find the first decreasing string. If you have a pivot point, now from right find the number greater than pivot. swap these two.
            Once that swap is done, reverse everthing starting from right of pivot.

            Time complexity : O(N)
            Space complexity : O(1)
"""

class Solution:
    def nextPermutation(self, a: str) -> str:
        """
        Strings immutable so converting to list
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        str_list = list(a)
        #doing a lamda to convert to ord
        str_list = [ord(x) for x in str_list]
        #find first decreasing from right
        pivot = -1
        for i in range(len(str_list)-1, 0, -1):
            if str_list[i] > str_list[i-1]:
                pivot = i-1
                break
        #finding number just larger than pivot to the right
        if pivot >-1:
            swap_pos = len(str_list)-1            
            while str_list[swap_pos] <= str_list[pivot]:
                #print(pivot, swap_pos)
                swap_pos-=1
            swap(str_list, pivot, swap_pos)
            
        pivot+=1
        swap_pos = len(str_list)-1
        while pivot < swap_pos:
            swap(str_list, pivot, swap_pos)
            pivot+=1
            swap_pos-=1
        #convert back to string
        str_list = [chr(x) for x in str_list]

        return "".join(str_list)


s= Solution()
print(s.nextPermutation("aaaaaa"))
print(s.nextPermutation("abc"))
print(s.nextPermutation("cba"))
print(s.nextPermutation("gfg"))
print(s.nextPermutation("aaaaabbbcbcbcbcd"))