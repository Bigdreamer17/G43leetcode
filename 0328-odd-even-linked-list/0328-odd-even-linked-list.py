# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        e = even = ListNode()
        o   = odd = ListNode()
        
        temp = head
        count = 0
        
        while temp:
            if count % 2 == 0:
                n = ListNode(temp.val)
                o.next = n
                o = o.next
            else:
                n = ListNode(temp.val)
                e.next = n
                e = e.next
            temp = temp.next
            count += 1
        o.next = even.next
        return odd.next