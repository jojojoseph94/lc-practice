"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

Solution : Merge one by one
            Time complexity : O(Nk) -> k lists, N elements each.
            Space complexity : Nk for results

         Heap - Add all first elements of all lists to heap, then pop minimum and add to result. 
                NOTE : for python3 heapq, to insert an object you can use tuple with (obj.val, obj) to add to heap. This ensures that obj.val is used to maintain the heap. But if 2 heap elements have same obj.val, then it uses the next element
                       in the tuple for comparison. But if that object does npt support comparion operator, which is true in this case, it is better to use a unique counter and that value for comparisons.
                Time complexity : O(Nlog(k)) -> k lists, N elements each.
                Space complexity : For heap k and kN for results.

"""

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #merge one by one
        if not lists:
            return None
        new_head = None
        for i in range(1,len(lists)):
            if new_head:
                list1 = new_head
            else:
                list1 = lists[0]
            list2 = lists[i]
            prev = None
            while list1 and list2:
                if list1.val < list2.val:
                    prev = list1
                    list1 = list1.next
                else:
                    temp = list2.next
                    list2.next = list1
                    if prev:
                        prev.next = list2
                    else:
                        new_head = list2
                    prev = list2
                    list2 = temp
            if list2:
                if prev:
                    prev.next = list2
                else:
                    new_head = list2
        if new_head:
            return new_head
        else:
            return lists[0]
                
    class Solution:
    def mergeKListsHeap(self, lists: List[ListNode]) -> ListNode:
        #merge one by one
        if not lists:
            return None
        new_head = None
        heap = []
        heapq.heapify(heap)
        #adding first elements to min heap
        #maintaining a counter for duplicate elements
        counter = 0
        for l in lists:
            if l:
                k = (l.val, counter, l)
                counter+=1
                heapq.heappush(heap, k)
        prev = None
        while heap:
            val, c, node = heapq.heappop(heap)
            if new_head == None:
                new_head = node
            if prev:
                prev.next = node
            prev = node
            if prev.next:
                counter+=1
                k = (prev.next.val, counter+1, prev.next)
                heapq.heappush(heap, k)
        return new_head