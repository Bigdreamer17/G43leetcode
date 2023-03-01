# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        # Base case = either of the node.next == None
        # State = 
        # Recurrence relation = 
        dummy = ListNode()
        result = dummy
        
        def merge(list1, list2, result):
            # Base Case
            if list1 == None and list2 == None:
                return dummy.next
            
            if list1 and not list2:
                result.next =  list1
                return dummy.next  
            if not list1 and list2:
                result.next = list2
                return dummy.next
                
            # Recursive relation
            if list1.val <= list2.val:
                result.next = list1
                result = result.next
                return merge(list1.next, list2, result)
            
            else:
                result.next = list2
                result = result.next
                return merge(list1, list2.next, result)
            
        return merge(list1, list2, result)
        
#         result = ListNode()
#         ans = result

#         while list1 and list2:
#             if list1.val <= list2.val:
#                 result.next = ListNode(list1.val)
#                 list1 = list1.next
#             else:
#                 result.next = ListNode(list2.val)
#                 list2 = list2.next
#             result = result.next

#         if list1:
#             result.next = list1
#         if list2:
#             result.next = list2
        
#         return ans.next