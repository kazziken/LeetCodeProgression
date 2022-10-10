# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 
        Maintain a hashSet, take the node in a for loop and add it to a set
        Take "visited nodes" and if it has already been visited "visited twice"
        -means you've detected a cycle - return True
        - use a fast and slow pointer
        - slow goes by 1
        - fast goes by 2
        - eventually the fast pointer is going to meet with the slow pointer
        - the time it takes for the Fast pointer to iterate through the whole cycle is n-1
        """
        
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False