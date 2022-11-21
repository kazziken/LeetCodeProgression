class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0: return res
        
        row_begin = col_begin = 0
        row_end = len(matrix) - 1 
        col_end = len(matrix[0]) - 1
        
        while (row_begin <= row_end and col_begin <= col_end):
            res += [matrix[row_begin][col] for col in range(col_begin, col_end + 1)]
            row_begin += 1
            res += [matrix[row][col_end] for row in range(row_begin, row_end + 1)]
            col_end -= 1
            
            if (row_begin <= row_end):
                res += [matrix[row_end][col] for col in range(col_end, col_begin - 1, -1)]
                row_end -= 1
                
            if (col_begin <= col_end):
                res += [matrix[row][col_begin] for row in range(row_end, row_begin - 1, -1)]
                col_begin += 1
        
        return res