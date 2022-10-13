# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        leftToRight = True
        while queue:
            levelSize = len(queue)
            currentLevel = deque()
            for _ in range(levelSize):
                currentNode = queue.popleft()

              # add the node to the current level based on the traverse direction
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)

                  # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(list(currentLevel))
            # reverse the traversal direction
            leftToRight = not leftToRight

        return result
            
                
        