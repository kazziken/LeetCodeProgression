# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS approach
        # definitely use a queue then add to output list
        res = []
        
        if root is None:
            return []
        
        queue = deque([root])
        
        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            res.append(currentLevel)
        return res
            
                
            
        
        
        