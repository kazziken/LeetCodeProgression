# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        
        #two pointers that will fix the final connection (when right passes left)
        tail, con = cur, prev
        while right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            right -=1
        
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
        
        
            
            