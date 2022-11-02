# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        """
        how to know you're at the nth position from the head node?
        [1,2,3,4,5]
         ^ 
        head
        """
        
        for i in range(n):
            fast = fast.next
            # if fast.next == None:
            #     slow.next == slow.next.next
            
            
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head