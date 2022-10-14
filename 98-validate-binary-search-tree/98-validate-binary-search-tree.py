# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we do a recursive call
        
        def valid(node, left, right):
            if not node:
                #because an empty binary tree is still a binary tree
                return True
            if not (node.val < right and node.val > left):
                #because we found a node that breaks the binary search tree
                return False
            
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )
            
        return valid(root, float("-inf"), float("inf"))