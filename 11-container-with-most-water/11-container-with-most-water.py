class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force is to try every possible combination with two pointers
        #my guess is to find the highest height then find the one furthest with similar height (for most amount of volume)
#         left, right = 0, len(height -1)
        
        
#             water = left * right 
#         return water
#         res = 0 #establish area in brute force method
        
#         for l in range(len(height)):
#          #left will be at every position at least once
#             for r in range(l + 1, len(height)):
#                 area = (r - l) * min(height[l], height [r])
#                 res = max(res, area)
#         return res
#         this was TLE

        #lets use a two pointer technique, one at the right, one at the left LIKE WE THOUGHT
        maxArea = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height [r])
            maxArea = max(area, maxArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea    
                                
        