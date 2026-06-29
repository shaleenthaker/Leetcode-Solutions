"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list."""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        while list1 and list2: # While there are still objects in both lists
            if list1.val <= list2.val: # If the current node in list1 is smaller, it goes in the joint list
                current.next = list1
                list1 = list1.next
            else: # Otherwise list2's node goes in the joint list
                current.next = list2
                list2 = list2.next

            current = current.next # Update current

        if list1: # Add the trailing ends of list1 or list2 to the end of the joint list
            current.next = list1
        else:
            current.next = list2

        return dummy.next # dummy's head was set to 0 by default, which we don't want in the return