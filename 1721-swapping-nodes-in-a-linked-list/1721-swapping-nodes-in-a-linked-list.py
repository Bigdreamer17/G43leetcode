# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Convert Linked list to list
        ll = []
        while head:
            ll.append(head.val)
            head = head.next
       # Two pointers to swap
        left = k - 1
        right = -k
        # Swapping
        ll[left], ll[right] = ll[right], ll[left]
        # Convert our list to linked list
        cur = dummy = ListNode(0)
        for i in ll:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next