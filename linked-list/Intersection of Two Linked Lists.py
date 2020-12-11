"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Solution : 1. Hashmap -> Navigate over first linked list keeping elements in hm
                         Then navigate over second looking to see if this node is already there
                         in hashmap. If yes that's where intersection begins
            Time complexity : O(N)
            Space complexity : O(N)
           2. 2 pointers for 2 linked lists. Iterate one node at a time till 2 pointers are not same
              If you reach end of one linked list, start from the beginning of other node
              Time complexity : O(N)
              Space complexity : O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        node = headA
        while node:
            node_set.add(node)
            node = node.next
        node = headB
        while node:
            if node in node_set:
                return node
            node = node.next
        return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #2 pointers
        pA = headA
        pB = headB
        while pA!=pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA

        