# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        # Computing the length
        leng = 0
        curr = head
        while curr:
            curr = curr.next
            leng += 1
        
        # Making it cirular linked list
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = head
        
        # Traversing len - k times and making its next == head
        # Then returning Head
        k = k % leng
        k = leng - k
        
        cur = head
        while k - 1 > 0:
            cur = cur.next
            k -= 1
        head = cur.next
        cur.next = None
        
        return head