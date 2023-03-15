# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def swap(head):
            if head is None or head.next is None:
                return head
            
            new_head = head.next.next
            curr_head = head.next
            
            # swapping
            head.next.next = head
            head.next = swap(new_head)
            
            return curr_head 
    
        return swap(head)