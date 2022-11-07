class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array first
        nums.sort()
        """
        nums = [-1,0,1,2,-1,-4]
        becomes
        nums = [-4,-1,-1,0,1,2]
        """
        triplets = []
        for left in range(len(nums) -2):
            if left > 0 and nums[left] == nums[left-1]: #avoid same nums
                continue    
            right = len(nums) -1
            mid = left + 1
            while mid < right:
                current_sum = nums[left] + nums[mid] + nums [right]
                if current_sum < 0:
                    mid += 1
                elif current_sum > 0:
                    right -=1
                else:
                    triplets.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[right] == nums[right - 1]:
                        right -=1
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid +=1
                    mid += 1
                    right -=1
        return triplets
