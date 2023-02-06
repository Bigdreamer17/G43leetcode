# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ll = []
        for i in lists:
            cur = i
            while cur:
                ll.append(cur.val)
                cur = cur.next
        ll.sort()
        
        curr = dummy = ListNode(0)
        for i in ll:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next