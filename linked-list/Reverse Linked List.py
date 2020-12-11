"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Solution : Iterative -> At each node, reverse the link by modifying next pointer to point to the previous node. 
                        After reversal, update previous to current node. And move to the next node to process.
            Time complexity : O(N)
            Space complexity : O(1)

            Recursive -> Recurse till back of the linked list.
            From the back of the list, reverse each link, and return the new head at each point.
            Time complexity : O(N)
            SPace complexity : O(N) (Recursive stack)

            Linked list         1-> 2-> 3
            head :              1->2
            rev :               2
            pt :                3->2
            head.next = None :  1->None
            rev.next = head :   2->1
            return pt :         3->2->1

"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        rev = head.next
        pt = self.reverseList(head.next)
        head.next = None
        rev.next = head
        return pt
        