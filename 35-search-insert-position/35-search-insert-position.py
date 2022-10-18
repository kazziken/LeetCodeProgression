class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #use binary search
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l += 1
            if nums[mid] > target:
                r -= 1
        return l
        