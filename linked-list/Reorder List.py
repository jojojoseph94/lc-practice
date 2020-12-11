"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


Solution : 

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find midpoint?
        #then reverse the ones till end
        #then merge them?
        if not head:
            return head
        def reverse(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev
        slow = head
        fast = head
        prev = None
        while fast:
            if fast.next == None:
                break
            fast = fast.next.next
            prev = slow
            slow = slow.next
        head2 = slow
        if prev == None:
            return head
        prev.next = None
        #reverse the second list
        head2 = reverse(head2)
        #merge the two lists
        node1 = head
        node2 = head2
        prev = None
        while node1 and node2:
            tmp = node1.next
            prev =node2
            node1.next = node2
            tmp2 = node2.next
            node2.next = tmp
            node1 = tmp
            node2 = tmp2
        if node2:
            prev.next = node2
        return head