# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if root is None:
            return []
        
        queue = deque([root])
        leftToRight = True
        
        while queue:
            currentLevel = deque()
            for i in range(len(queue)):
                currentNode = queue.popleft()
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            res.append(list(currentLevel))
            leftToRight = not leftToRight
        return res
            
                
        