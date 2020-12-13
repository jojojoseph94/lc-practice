"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Solution : Keep a seen hashmap of letters alon gwith their indexes which gets updated at each point. 
           If you have seen this letter before and it is after the current start point, update the start point.
           At each point the answer gets updated as ans = max(ans, length of the current longest string - which is i - start + 1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        start = 0
        ans = 0
        for i in range(0,len(s)):
            if s[i] in hm and hm[s[i]] >= start:
                start = hm[s[i]]+1
            hm[s[i]] = i
            ans = max(ans, i - start +1)
        return ans