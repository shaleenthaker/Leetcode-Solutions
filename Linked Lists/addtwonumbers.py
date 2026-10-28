"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        currVal = 0
        carry = False
        output = ListNode()
        head = output
        while l1 or l2:
            output.next = ListNode()
            output = output.next
            if l1:
                currVal += l1.val
                l1 = l1.next
            if l2:
                currVal += l2.val
                l2 = l2.next
            if carry:
                currVal += 1
            if currVal >= 10:
                currVal %= 10
                carry = True
            else:
                carry = False
            output.val = currVal
            currVal = 0
        if carry:
            output.next = ListNode(1)
        return head.next