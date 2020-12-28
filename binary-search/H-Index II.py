"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?


Solution : Binary search -> left, right mid. Now at mid, the citations[mid] gives the number of citations, and N-mid gives the number of papers with >=citations[mid] citations.
                             So, if citations[mid] is equal to N-mid, that is the answer.
                             If not move left if the citations[mid] is greater than the number of papers to the right of mid.
                             Move right if the citations[mid] is less than the number of papers to the right of mid.
                             Finally return N-left as answer
            Time complexity : O(log(N))
            Space complexity : O(1)
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        N = len(citations)
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] == N-mid:
                return citations[mid]
            elif citations[mid] > N-mid:
                right = mid-1
            else:
                left = mid + 1
        return N- left