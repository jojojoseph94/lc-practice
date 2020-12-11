"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Solution : 1. use a hashmap and keep visiting nodes to find the entry to the cycle
            Time complexity : O(N)
            Space complexity : O(N)
           2.Floyds hare and tortoise -> Start at head, 2 pointers, one fast and one slow. Find the cycle.
             After finding the cycle, reset the slow to head and keep moving slow and fast one node at a time to find the entry to cycle.
             Time complexity : O(N)
             Space complexity : O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        #detect cycle
        slow = head
        fast = head
        while 1:
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            else:
                #no cycle
                return None
            slow = slow.next
            if slow == fast:
                break
        #cycle -> reset slow to head
        #the point at which slow and fast meet again is the point of start of cycle
        #floyds tortoise and hare algo
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow