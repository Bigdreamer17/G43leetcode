# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head 
        
        # Spliting in the middle
        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        
        # Reversing the head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Calculating the sum
        left = prev
        right = sec
        summ = 0
        while left and right:
            summ = max(summ, left.val + right.val)
            left = left.next
            right = right.next
        return summ