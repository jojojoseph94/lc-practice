"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

Solution 1 : For both s and t, create hashmaps, which keep track of the indexes at which each char occurs.
             eg, abba, bbaa
                 hm1 will be {a: [0,3], b: [1,2]} and hm2 will be {a: [2,3], a: [0,1]}
                 Now get the values and sort it by the vals.
                 So it will be val1 = [[0,3], [1,2]] and val2 = [[0,1], [2,3]]
                 Now check if both are equal.
            Time complexity : O(N)
            Space complexity : O(Nlog(N)) -> since sorting is involved.

Solution 2: At each point, assume you are replacing the character at s with the character at t.
            This will work only if they are isomorphic. Hence at each point, see if you had used this character before.
            This can be done by using two hashmaps, one for s to t transformation, and one for the reverse transformation.

            Why do you need to check both ways? ab and aa case. If you check only ab to aa case, there won't be any issues
            since you will use a for both a and b, which is wrong

            Time complexity : O(N)
            Space complexity : O(N)

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        hm1 = {}
        hm2 = {}
        for i in range(len(s)):
            hm1[s[i]] = hm1.get(s[i], []) + [i]
            hm2[t[i]] = hm2.get(t[i], []) + [i]
        return sorted(hm1.values()) == sorted(hm2.values())

    def isIsomorphicBetter(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True