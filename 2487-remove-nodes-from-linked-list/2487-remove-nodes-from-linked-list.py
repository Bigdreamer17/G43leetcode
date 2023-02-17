# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
        
        maxx = 0
        for i in range(len(stack)-1, -1, -1):
            if stack[i] > maxx:
                maxx = stack[i]
            elif stack[i] < maxx:
                stack.pop(i)
            else:
                continue
        
        cur = dummy = ListNode()
        for i in stack:
            cur.next = ListNode(i)
            cur = cur.next
        
        return dummy.next
        