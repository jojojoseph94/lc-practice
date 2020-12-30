"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

Solution : There are 3 solutions - 
            1. Bruteforce - All substrings, check if palindrome . O(N^3) solution (O(N^2) for generating all substrings and O(N) again for checking if palindrome)
            2. DP - Here we are keeping track of all the palindromes in a dp array. 
               c a a b a a d
           c [ T F F F F F F]
           a [ F T          ] 
           a [ F   T        ]
           b [ F     T      ]
           a [ F       T    ]
           a [ F         T  ]
           d [ F           T]

            dp[i][j] -> Is the string s[i:j+1] a palindrome?
            To figure this out fill in the entries for single length string and 2 lenght string. Then for 3 length to the rest, use the dp fomrmula
                dp[i][j] = dp[i+1][j-1] and s[i]==s[j]

            Time complexity : O(N)
            Space complexity : O(N)

            3. Expand from center - Here at each point we are building the palindrome from the center. You can either have the odd letter palindrome or even letter palindrome.
               So we try both and compare with the answer.
            Time complexity : O(N)
            Space complexity : O(1)

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalidrome(i,j):
            while i>=0 and j <len(s) and s[i] == s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        #expand around center
        ans = ""
        for i in range(0,len(s)):
            #check if this can be center of a palindrome
            p1 = checkPalidrome(i,i)
            if i+1 < len(s):
                p2 = checkPalidrome(i,i+1)
            else:
                p2 = ""
            #print("For ",i,p1,p2)
            if len(p2) > len(p1):
                p1 = p2
            if len(p1) > len(ans):
                ans = p1
        return ans

        def longestPalindromeDP(self, s: str) -> str:
        if not s:
            return s
        ans = ""
        l = 0
        r = 0
        dp = [[False]*len(s) for _ in range(0,len(s))]
        dp[-1][-1] = True
        for i in range(0,len(s)-1):
            dp[i][i] = True
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                l = i
                r = i+1
        for m in range(2,len(s)):
            for i in range(len(s)-m):
                j=i+m
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i > r-l:
                    l = i
                    r = j
        return s[l:r+1]