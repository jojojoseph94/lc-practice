"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Solution : Maintain stack with all starting brackets. Once an ending bracket is seen, see if it has a correspoding starting bracket at top. 
            Once done with all symbols, see if stack is empty

            Time complexity : O(N)
            Space complexity : O(N)

"""

class Solution:
    def isValid(self, s: str) -> bool:
        starts = {"}": "{", ")" : "(", "]": "["}
        stack = []
        for p in s:
            if p == "[" or p == "{" or p == "(":
                stack.append(p)
            else:
                if not stack:
                    return False
                b = stack.pop()
                if starts[p] != b:
                    return False
        if stack:
            return False
        return True