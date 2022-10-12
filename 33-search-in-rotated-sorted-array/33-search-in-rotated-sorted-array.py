class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        thoughts:
        to find the pivot point by binary search then go for the correct half to perform another round of binary search 
        until target is found
        
        we need the target to find pivot point
        
        """
        
        
        left, right = 0, len(nums) -1 
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1