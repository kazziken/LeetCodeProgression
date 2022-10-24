# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        since I looked at discussion tab for ans
        
        create a new array []
        append head then everytthing after
        then if that arr == head[::-1]
        RETURN TRUE
        
        """
        
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]