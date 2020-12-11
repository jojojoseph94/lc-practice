"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.

Solution : Keep a hashmap of longer string with counts. Then for the smaller string, iterate over the letters checking to see if its there in the longer one.
           If there, add it to the result based on the number of times it occurs. Delete the key from the hashmap. After done with the short string, check if any
           keys remain in hashmap. If yes add them to result based on the number of times it occurs.

           Time complexity : O(N)
           Space complexity : O(1) -> 26 letters
"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        hm = {}
        for letter in T:
            hm[letter] = hm.get(letter, 0) + 1
        res = ""
        for letter in S:
            if letter in hm:
                res += letter*hm[letter]
                del hm[letter]
        for key in hm.keys():
            res += key*hm[key]
        return res