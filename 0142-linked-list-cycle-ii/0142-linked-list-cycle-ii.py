# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        # flyod cyle finding algorithm 
        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        # if no loop exists
        if slow !=  fast:
            return "no cycle"
        # reset slow pointer to head
        # and traverse again
        while head != slow:
            head = head.next
            slow = slow.next

        return head