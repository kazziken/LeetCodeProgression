# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         if root is None:
#             return []
        
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        res = []
        stack = []
                
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                topNode = stack.pop()
                res.append(topNode.val)
                root = topNode.right
        return res

            

            
            
    
        

        