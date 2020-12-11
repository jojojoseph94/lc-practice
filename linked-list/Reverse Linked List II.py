"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Solution : Use regular reverse from m to n
            But after reverse, return rev_head, rev_tail and next_node after rev_head

            So in this case, after reverse, 4->3->2, 4 is reverse head, 2 is reverse tail and 5 is the node after rev_head
            These are needed so that we can stitch this list to the main list

            So in main list the node before reversal began, prev is 1;

            So 1.next = rev_head
                1-> 4->3->2
            and rev_tail.next is next node after rev_head hence
                2->5
            So final list is
            1->4->3->2->5->NULL

            Time complexity : O(N)
            Space complexity : O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(head, i, n):
            node = head
            prev = None
            while node and i <= n:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i+=1
            return [prev, head, node]

        i = 1
        node = head
        prev = None
        while i < m:
            prev = node
            node = node.next
            i+=1
        #reverse from here till n
        rev_head, rev_tail, next_node = reverse(node, i, n)
        if next_node:
            rev_tail.next = next_node
        if prev:
            prev.next = rev_head
            return head
        else:
            return rev_head


                