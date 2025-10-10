# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mindpoint, delink and assign it to list2
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        # Reverse list2
        prev, curr = None, list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list2 = prev

        # Merge list2 into list1
        curr1 = head
        curr2 = list2
        prev1, prev2 = None, None

        while curr2:
            prev1 = curr1
            curr1 = curr1.next
            prev2 = curr2
            curr2 = curr2.next
            prev1.next = prev2
            prev2.next = curr1
        
        return head

