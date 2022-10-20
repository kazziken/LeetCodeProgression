# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
    #solving using Depth First Search(DFS) - using a STACK
        
#         stack = [[root, 1]] #depth is 1
#         result = 0
        
#         while stack:
#             node, depth = stack.pop()
            
#             if node:
#                 result = max(result, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
                
#         return result
        
        