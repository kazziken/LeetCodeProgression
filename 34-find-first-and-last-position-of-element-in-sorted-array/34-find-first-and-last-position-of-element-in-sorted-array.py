class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
                
        start = self.find_Starting_Index(nums, target)
        end = self.find_Ending_Index(nums,target)
        
        return [start,end]
    
    def find_Starting_Index(self, nums ,target):
        index = -1
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                index = mid
                right = mid - 1 # this will start to find the ending index
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return index
    
    def find_Ending_Index(self, nums ,target):
        index = -1
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                index = mid
                left = mid + 1 # this will start to find the ending index
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return index
        
        