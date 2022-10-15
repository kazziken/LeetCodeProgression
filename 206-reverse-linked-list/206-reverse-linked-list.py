# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        
        while current:
            #set old current.next to a variable
            next = current.next
            # current.next is now previous
            current.next = previous
            # previous now is the current
            previous = current
            # current is now current.next
            current = next
            #repeat til current is null that is pointing at the head
        return previous