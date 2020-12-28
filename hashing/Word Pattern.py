"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

Solution : Similar to Isomorphic strings. Keep 2 hashmaps, one for pattern to word transformation and one for word to pattern transformations.
           At each point, check to see if this word or pattern was used before and if so is the current transformation the same as before. 
           If not, return False.
           Update the hashmaps with the transformations done, for both hashmaps

           Time complexity : O(N) -> enumerating over the entire pattern/ words
           Space complexity : O(N) -> 2 hashmaps

#TODO You can also do this using a single hashmap. Store both transformations in the same hashmap?
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!=len(pattern):
            return False
        pat2w = {}
        w2pat = {}
        for index, char in enumerate(pattern):
            if char in pat2w and pat2w[char]!=s[index]:
                return False
            if s[index] in w2pat and w2pat[s[index]]!=char:
                return False
            pat2w[char] = s[index]
            w2pat[s[index]] = char
        return True