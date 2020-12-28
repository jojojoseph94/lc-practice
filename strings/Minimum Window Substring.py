"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?

Solution : Bruteforce - for all substrings, check if the substring contains all characters of t.
           Time complexity : O(n^2)
           Space complexity : O(len(t))

           Optimized : Keep a window to which you add characters to right. Keep checking to see if all characters of t are present.
                       While all characters are present, remove one by one from left narrowing the window. If all characters are not present, keep adding
                       characters to the right
            Time complexity : O(N)
            Space complexity : O(len(t))
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        ans_start = -1
        ans_end = -1
        ans_len = float('inf')
        formed = 0
        required = len(t_counter.keys())
        left = 0
        right = 0
        window_chars = {}
        while right < len(s):
            window_chars[s[right]] = window_chars.get(s[right], 0) + 1
            if s[right] in t_counter and window_chars[s[right]] == t_counter[s[right]]:
                    formed+=1
            while formed == required:
                if ans_len > (right - left):
                    ans_len = (right - left)
                    ans_start = left
                    ans_end = right
                    #remove char from left
                window_chars[s[left]]-=1
                if s[left] in t_counter and window_chars[s[left]] < t_counter[s[left]]:
                    formed-=1
                left+=1
            right+=1
                                
        if ans_len == float('inf'):
            return "" 
        else:
            return s[ans_start:ans_end+1]