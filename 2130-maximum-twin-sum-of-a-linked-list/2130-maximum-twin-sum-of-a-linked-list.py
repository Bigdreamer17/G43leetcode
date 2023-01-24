# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        values = []
        while head:
            n += 1
            values.append(head.val)
            head = head.next
        summ = []
        for i in range(len(values)):
            summ.append(values[i] + values[n-1-i])
        
        return max(summ)