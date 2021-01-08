"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Solution : 1. From back, keep track of the last time when each temperature occurs. And process the list from last adding answers to a deque.
               update the occurance of temperature at each point.

            Time complexity : O(N)
            Space complexity : O(K), where K is the range of temperatures we keep track of
        
            2. Using stack. Use a stack to keep track of indexes of temperatures above the current one. Start processing from the end too. At each point check if stack has something smaller than current temp. If so, then keep popping.
            This way you may be able to save some space if temp range is too large.

"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = collections.deque()
        temps = [None]*101
        for i in range(len(T)-1,-1,-1):
            d = 0
            for t in range(T[i]+1, 101):
                if temps[t] and temps[t] > i:
                    if d == 0:
                        d = temps[t] - i
                    else:
                        d = min(d, temps[t]-i)
            temps[T[i]] = i
            ans.appendleft(d)
        return ans