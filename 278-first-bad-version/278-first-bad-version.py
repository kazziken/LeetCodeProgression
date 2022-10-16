# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        say we need to find a point in an array where you have no idea where it went to shit
        in this case
        use binary search to find the midpoint
        if midpoint is not a badVersion -> right
                because it hasnt been bad yet
        if midpoint is a badVersion -> left
        
        we need to return the output of where badVersion is
        ex: [1,2,3,4,5]
        """
        
        l, r = 1, n
        
        while l != r:
            mid = (r - l) // 2 + l
            
            if not isBadVersion(mid):
                l = mid+1
            else:
                r = mid
        return l or r