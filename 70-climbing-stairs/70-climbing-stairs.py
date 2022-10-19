class Solution:
    def climbStairs(self, n: int) -> int:
#         a, b = 1, 0
        
#         for _ in range(n):
#             a, b = b+a, a
#         return a
        
    #O(n) space
    
        if n == 1:
            return 1
        #create empty list
        res = [0 for i in range(n)]
        res[0], res[1] = 1,2
        
        for i in range(2,n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
        