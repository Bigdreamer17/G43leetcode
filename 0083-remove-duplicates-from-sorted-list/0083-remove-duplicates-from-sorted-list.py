# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        # right = head.next
        
        while left and left.next:
            if left.val == left.next.val:
                left.next = left.next.next
            else:
                left = left.next
        return head