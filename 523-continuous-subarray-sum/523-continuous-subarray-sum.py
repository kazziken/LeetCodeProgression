class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {} # can also write {0:0}
        sum = 0
        i = 0
        hashMap[0] = 0
        
        
        
        for i in range(len(nums)):
            sum += nums[i]
            if sum % k not in hashMap:
                hashMap[sum%k] = i + 1
            elif hashMap[sum%k] < i:
                return True
        return False