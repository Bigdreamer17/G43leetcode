# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # using Monotonic stack
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        monstack = []
        nextGreater = {i:0 for i in  range(len(stack))}
        for i in range(len(stack)):
            
            while monstack and stack[monstack[-1]] < stack[i]:
                nextGreater[monstack.pop()] = stack[i]
            monstack.append(i)
        return [nextGreater[i] for i in nextGreater]      
        