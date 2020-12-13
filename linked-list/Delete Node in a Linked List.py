"""
Delete a Node from linked list without head pointer
You are given a singly linked list and pointer which is pointing to the node which is required to be deleted.
Any information about head pointer or any other node is not given. You need to write a function to delete that node from linked list.
Your function will take only one argument: pointer to the node which is to be deleted.

Solution : Copy the next nodes data to the current node

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNode(self, node: ListNode):
        next_node = node.next
        if next_node:
            node.val = next_node.val
            node.next = next_node.next
            del next_node 
        else:
            #last node
            #needs previous node
            return