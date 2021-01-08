"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

Solution : Heap -> Store ugly numbers in an array. Use a set to store the seen ugly numbers. Initialize the ugly list with 1. Put 1 in min heap. At each point, pop the minimum element from the heap, add it to your answer list, and add the ugly number *2, ..*3, ..*5 to the heap 
                   (to avoid duplicates we are using a set)

                   Time complexity : O(Nlog(N)) - (to maintain heap - here N won't exeeed 1690 according to question)
                   Space complexity : O(N) for heap and for seen set

           This can also be done using an array and pointers
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        if n < 2:
            return ugly[0]
        heap = []
        heapq.heapify(heap)
        seen = set()
        for u in ugly:
            if u*2 not in seen:
                heapq.heappush(heap, u*2)
                seen.add(u*2)
            if u*3 not in seen:
                heapq.heappush(heap, u*3)
                seen.add(u*3)
            if u*5 not in seen:
                heapq.heappush(heap, u*5)
                seen.add(u*5)
        while len(ugly) < n:
            u = heapq.heappop(heap)
            ugly.append(u)
            if u*2 not in seen:
                heapq.heappush(heap, u*2)
                seen.add(u*2)
            if u*3 not in seen:
                heapq.heappush(heap, u*3)
                seen.add(u*3)
            if u*5 not in seen:
                heapq.heappush(heap, u*5)
                seen.add(u*5)
        return ugly[-1]