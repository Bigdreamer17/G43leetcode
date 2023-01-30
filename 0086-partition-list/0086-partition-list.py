# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        below = []
        above = []
        
        while head:
            if head.val  < x:
                below.append(head.val)
            else:
                above.append(head.val)
            head = head.next
        below.extend(above)
        
        cur = dummy = ListNode(0)
        for i in below:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next