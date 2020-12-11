"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass? 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Solution : 2 pass -> just find the length in 1st pass and then delete (L-N-1)th node in second pass
           1 pass -> use 2 pointers, one which is N nodes ahead (fast)
                     then advance one pointer each for slow and fast till end. Once at end, slow.next is the node we want to delete.
                     Take care of edge cases like deleting the first or last nodes.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #go n nodes head
        node = head
        slow = node
        fast = node
        while n:
            fast = fast.next
            n-=1
        #is this the end? if so delete the first one
        if not fast:
            del_node = head
            head = head.next
            del_node.next = None
            return head
        #now go till end
        while fast.next:
            fast = fast.next
            slow = slow.next
        #now delete
        del_node = slow.next
        #is this the last node I'm deleting?
        if del_node.next:
            slow.next = slow.next.next
            del_node.next = None
            return head
        else:
            #delete the last node
            slow.next = None
            return head