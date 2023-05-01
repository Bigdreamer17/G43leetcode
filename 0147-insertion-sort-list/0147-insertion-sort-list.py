# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, cur_prev, cur = ListNode(-1, head), head, head.next
        while cur:
            j_prev, j, cur_next = dummy, dummy.next, cur.next
            if cur.val > cur_prev.val:
                cur_prev = cur
            else:                
                while j.val < cur.val:
                    j_prev, j = j, j.next
                cur.next = j
                j_prev.next = cur
                cur_prev.next = cur_next
            cur = cur_next
        return dummy.next