"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

Solution : Keep a hashmap with key as a counter of letters. Create key for each letter and then add it to the corresponding 
            hashmap entry. Finally iterate over the keys and add the values to the result.

            Time complexity: O(NK) -> You have to iterate over every word. K letters in each word(?)
            Space complexity : O(NK) -> For results.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            hm_key = [0]*26
            for letter in word:
                hm_key[ord(letter)-ord('a')]+=1
            hm_key = tuple(hm_key)
            hm[hm_key] = hm.get(hm_key, []) + [word]
        ans = []
        for key in hm.keys():
            ans.append(hm[key])
        return ans