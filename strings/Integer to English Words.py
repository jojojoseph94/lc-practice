"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1

Solution : Find how many billionth, millionth, thousanth and rest position the number is.
            This is done by diving the number by billion, (num - billionth * billion)//million etc
            Then call function to print corresponding numbers as needed. (Numbers are usually passed to three digit handler)
            Time complexity : O(1)
            Space complexity : O(1)
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        def ones(n):
            one = {1:"One", 2:"Two", 3: "Three", 4: "Four", 5: "Five", 6:"Six", 7: "Seven", 8: "Eight", 9:"Nine"}
            if n in one:
                return one[n]
        def tens(n):
            ten = {10:"Ten", 11:"Eleven", 12:"Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16:"Sixteen", 17: "Seventeen", 18: "Eighteen", 19:"Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
            if n in ten:
                return ten[n]
        def two(n):
            if not n:
                return ''
            if n > 19:
                if n%10:
                    return tens((n//10)*10) + " " + ones(n%10)
                else:
                    return tens(n)
            elif n > 9:
                return tens(n)
            else:
                return ones(n)
        def three(n):
            hundreds = n//100
            rest = n - hundreds*100
            if hundreds:
                if rest:
                    return two(hundreds) + " Hundred " + two(rest)
                else:
                    return  two(hundreds) + " Hundred"
            else:
                return two(rest)
        
        ans = ""
        billion = num//1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = ((num - billion * 1000000000) - million* 1000000)//1000
        rest = (((num - billion * 1000000000) - million* 1000000) - thousand * 1000)
        #print(billion, million, million, thousand, rest, three(thousand))
        if not num:
            return "Zero"
        if billion:
            ans = three(billion) + " Billion"
        if million:
            if ans:
                ans = ans + " " + three(million) + " Million"
            else:
                ans = three(million) + " Million"
        if thousand:
            if ans:
                ans = ans + " " + three(thousand) + " Thousand"
            else:
                ans = three(thousand) + " Thousand"
        if rest:
            if ans:
                ans = ans + " " + three(rest)
            else:
                ans = three(rest)
        return ans
            