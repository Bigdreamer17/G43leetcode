# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        while left < right:
            arr[left - 1], arr[right - 1] = arr[right - 1], arr[left - 1]
            left += 1
            right -= 1
        
        temp = dummy = ListNode(0)
        for i in arr:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next