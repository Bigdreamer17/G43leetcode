# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        ans = []
        summ = length = cur_pos = 0
        
        while head:
            head = head.next
            length += 1
        
        while cur_pos != length - 1:
            summ += cur.val
            if cur.val == 0:
                ans.append(summ)
                summ = 0
            cur = cur.next
            cur_pos += 1
        
        curr = dummy = ListNode(0)
        for i in ans:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
                
            
            