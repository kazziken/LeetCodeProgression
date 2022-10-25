class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        If we do fast and slow pointer
        slow pointer start at 0
        and slow pointer moving depending on the length of the list
        make fast pointer determine switching the numbers til all the 0s are in the beginning of the array
        and the rest of the nums are compared based on value
        """
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        