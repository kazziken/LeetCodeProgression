# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         if root is None:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
    #solving using Depth First Search(DFS) - using a Deque
        
        if root is None:
            return 0
        
        queue = deque([root])
        nodeLevel = 1
        levels = 0
        
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # subtract from nodeLevelwhile adding to levels to represent the BFS
            nodeLevel -=1
            if nodeLevel == 0:
                levels +=1
                nodeLevel = len(queue)
        return levels
        
        