"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

Solution : Keep track of prev operation and prev number at all times. Add a "+0" to the end of the string so that everything in stack is processed
           At each point check to see if number or symbol. If number, keep on creating the number.
           If symbol, then process the previous symbol and number. If * or / are the previous symbols, process and put to stack.
           Else just add the number to the stack with symbol.


           Finally sum up everything in the stack as result.
        Time complexity : O(N)
        Space complexity : O(N) -> stack size

"""
class Solution:
    def calculate(self, s: str) -> int:
        s+="+0"
        stack = []
        prev_op = "+"
        num = 0
        for char in s:
            if char == " ":
                continue
            elif char.isnumeric():
                num = num*10 + int(char)
            else:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    n2 = stack.pop()
                    stack.append(num * n2)
                else:
                    n2 = stack.pop()
                    stack.append(int(n2/num))
                prev_op = char
                num = 0
        return sum(stack)