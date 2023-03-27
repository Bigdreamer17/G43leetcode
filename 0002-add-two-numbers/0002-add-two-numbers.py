# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0

        res = ans = ListNode(0)

        while l1 or l2 or sum:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum , val = divmod(v1 + v2 + sum, 10)
            ans.next = ListNode(val)
            ans =ans.next
        
        return res.next
        
        
        
        
        
        
        
        
        