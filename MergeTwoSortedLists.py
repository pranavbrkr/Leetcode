# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = None
        curr = head
        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                if not head:
                    head = curr1
                    curr = head
                else:
                    curr.next = curr1
                    curr = curr.next
                curr1 = curr1.next
                curr.next = None
            else:
                if not head:
                    head = curr2
                    curr = head
                else:
                    curr.next = curr2
                    curr = curr.next
                curr2 = curr2.next
                curr.next = None

        if curr1 != None:
            if not head:
                head = curr1
            else:
                curr.next = curr1
        
        if curr2 != None:
            if not head:
                head = curr2
            else:
                curr.next = curr2

        return head