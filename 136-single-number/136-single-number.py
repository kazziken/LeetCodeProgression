class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Use hashmap to iterate through nums array
        key = num[value]
        value = times it shows up
        return nums[value] = 1
        NEVER MIND because we can only use o(1) space
        
        WE ARE USING BIT MANIPULATION
        
        [
        4, 100
        1, 001
        2, 010
        1, 001
        2 010
        ]
        """
        
        #store XOR  here
        res = 0 #n ^ 0 = n
        for n in nums:
            res = n ^ res 
        return res