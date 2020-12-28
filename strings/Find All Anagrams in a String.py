"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Solution : Keep 2 counters; use sliding window of size len(p) on s to maintina the s_counter. At each point, check if the counters are equal. If yes, add index to ans.
Time complexity : O(N)
space complexity : O(1) - 26 characters

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = Counter()
        ans = []
        for i in range(len(s)):
            #print(s_counter, p_counter)
            s_counter[s[i]]+=1
            if i >= len(p):
                #remove a char from left
                s_counter[s[i-len(p)]]-=1
                if s_counter[s[i-len(p)]] == 0:
                    del s_counter[s[i-len(p)]]
            if s_counter == p_counter:
                ans.append(i-len(p)+1)
        return ans