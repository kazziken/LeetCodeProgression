# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def depth(self, node: Optional[TreeNode]):
        
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        
        if left + right > self.diameter:
            self.diameter = left + right
        #makes sure the parent node(s) get the correct depth from this node
        return 1 + (left if left > right else right)
    
    def diameterOfBinaryTree(self, root):
        if root is None: return 0
        
        self.depth(root)
        return self.diameter
    