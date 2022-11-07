# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None
        
        while current:
            #set old current.next to a variable
            next = current.next
            # current.next is now previous WHICH IS NONE so it looks like 
            # null <- 1 -> 2 -> 3 -> 4
        #current.next 
            current.next = prev
            # previous now is the current
            prev = current
            # current is now current.next
            current = next
            #repeat til current is null that is pointing at the head
        return prev