# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Can this be a DFS? - using Stack
        or using recursion
        """
        
        #RECURSION
        if root is None:
            return True
        
        
        return self.is_reverse(root.left, root.right)
    
    def is_reverse(self, a, b):
        if not a or not b:
            return not a and not b
        return a.val == b.val and self.is_reverse(a.left,b.right) and self.is_reverse(a.right,b.left)      

        #Iteratively
        
#         if root is None:
#             return True
        
#         stack = [[root.left , root.right]]
        
#         while len(stack)>0:
#             pair = stack.pop(0)
#             left = pair[0]
#             right = pair[1]
            
#             if left is None and right is None:
#                 continue
#             if left is None or right is None:
#                 return False
            
#             if left.val == right.val:
#                 stack.insert(0, [left.left, right.right])
#                 stack.insert(0, [left.right, right.left])
#             else:
#                 return False
#         return True
            