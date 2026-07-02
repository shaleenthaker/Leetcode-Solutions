"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Tortoise and Hare algorithm: move Tortoise forward by one in each iteration, move Hare forward by two. If there is a cycle, they will be equal in n iterations

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        while True:
            if head is None:
                return False
            head = head.next
            if head is None:
                return False
            head = head.next
            slow = slow.next
            if slow == head:
                return True