class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix) 
        
        while left < right and top < bottom:
            # left to right
            # get every value in top row
            
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1 # this is shifting top down one
            
            for i in range(top, bottom):
                res.append(matrix[i][right - 1]) #because right is out of bounds
            right -= 1
            
            if not(left < right and top < bottom):
                break
            
            for i in range(right - 1, left -1, -1): #dont want to include already traversed elements
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
                
                
            
            