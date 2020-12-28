"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
Absolute value of elements in the array and x will not exceed 104

Solution : BINARY SEARCH but with left 0 and right k elements to the left of last element.
            Same binary search with mid value, but move to left or right based on difference between target and mid value and , [mid+k] value and target.

            Assume A[mid] ~ A[mid + k] is sliding window

            case 1: x - A[mid] < A[mid + k] - x, need to move window go left
            -------x----A[mid]-----------------A[mid + k]----------

            case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
            -------A[mid]----x-----------------A[mid + k]----------

            case 3: x - A[mid] > A[mid + k] - x, need to move window go right
            -------A[mid]------------------x---A[mid + k]----------

            case 4: x - A[mid] > A[mid + k] - x, need to move window go right
            -------A[mid]---------------------A[mid + k]----x------

            If x - A[mid] > A[mid + k] - x,
            it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
            and we have mid smaller than the right i.
            So assign left = mid + 1.

            Important
            Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
            It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3

            If A[mid] == A[mid + k], we do not know whether we should move left or right when checking the absolute value.
            So, if you really want to use abs, add logic for arr[mid] == arr[mid + k], eg:

                if (arr[mid] == arr[mid + k]) {  // <---- add this
                    if (x > arr[mid])
                        left = mid + 1;
                    else
                        right = mid;
                } else if (Math.abs(arr[mid]-x) > Math.abs(arr[mid+k]-x))
                    left = mid + 1;
                else
                    right = mid;

            Time complexity : O(log(N))
            Space complexity : O(1)

            
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-k
        while left < right:
            mid = (left + right)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]