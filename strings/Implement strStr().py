"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

Solution 1 : 2 pointers - one for haystack and one for needle.
            While both are same, keep incrementing. When there is a mismatch,
            reset the needle to 0 and haystack to haystack - needle +1
           Time complexity : O(N*L)
           Space complexity : O(1)
Solution 2 : KMP algorithm - TODO
            Time complexity : O(N)
            Space complexity : O(1ß)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #2 pointers
        h_ptr = 0
        n_ptr = 0
        while h_ptr < len(haystack) and n_ptr < len(needle):
            if haystack[h_ptr] == needle[n_ptr]:
                h_ptr+=1
                n_ptr+=1
            else:
                #reset
                h_ptr -= n_ptr
                h_ptr+=1
                n_ptr = 0
        if n_ptr == len(needle):
            return h_ptr - n_ptr
        else:
            return -1