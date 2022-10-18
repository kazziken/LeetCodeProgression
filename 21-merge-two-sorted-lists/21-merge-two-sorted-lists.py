# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        #create a dummy node so you dont have to worry about the edge case of inserting a dummy 
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                #update pointer
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
            
            
        