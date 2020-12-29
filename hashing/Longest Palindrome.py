"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.


Solution : Greedy - all even numbers goes to answer. All odds, go to answer except one character. Then add one character to the answer
if you had an odd occuring character.

eg : abbaddaccc

    answer -> bdcaaacdb
            OR bdacccadb

Time complexity : O(N)
Space complexity : O(1), if no of alphabets is fixed.

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ans = 0
        odd = 0
        for key in counts.keys():
            if counts[key]%2==0:
                ans+=counts[key]
            else:
                ans+=counts[key]-1
                odd = 1
        return ans+odd