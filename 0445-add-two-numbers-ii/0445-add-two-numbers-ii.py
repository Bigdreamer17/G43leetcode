# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        ans = []
        
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        
        num1 = ''.join(num1)
        num2 = ''.join(num2)
        summ = int(num1) + int(num2)
        summ = str(summ)
        
        for i in summ:
            ans.append(int(i))
        
        cur = dummy = ListNode(0)
        for i in ans:
            cur.next = ListNode(i)
            cur = cur.next
        
        return dummy.next