"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            head = head.next
            cur.next = prev
            prev = cur
            cur = head
        return prev