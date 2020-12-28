"""
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

Solution : If negative power, just make it positive and change x to 1/x (Math)
            While power is greater than 0, keep multiplying the product to itslef, If power becomes odd, multiply product to answer. Half the power at each steps.
            Time complexity : O(log(N))
            Space complexity : O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1/x
            N = -N
        ans = 1
        cur_product = x
        while N >0:
            if N%2==1:
                ans = ans * cur_product
            cur_product*=cur_product
            N //=2
        return ans