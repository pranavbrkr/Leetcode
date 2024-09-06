# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_dict = {}

        for number in nums:
            if number not in nums_dict.keys():
                nums_dict[number] = True
        
        prev = None
        curr = head

        while curr:
            if curr.val in nums_dict.keys():
                if curr == head:
                    prev = curr
                    curr = curr.next
                    head = curr
                    prev.next = None
                    prev = None
                else:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head