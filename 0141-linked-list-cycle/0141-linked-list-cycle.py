# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Flyod cycle detection algorithm
        slowp = head
        fastp = head

        while slowp != None and fastp != None and fastp.next != None:
            slowp = slowp.next
            fastp = fastp.next.next

            if slowp == fastp:
                return True 
        return False