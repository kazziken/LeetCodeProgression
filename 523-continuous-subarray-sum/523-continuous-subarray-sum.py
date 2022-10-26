# For example for array [23,4,8] and k = 6 
# we can see for indices 1 and 2 we have a subarray [4,8] which satisfies the constraint
# sum([23,4]) = 27, 27 % 6 = 3
# sum([23,4,6]) = 33 % 6 = 3
# Which implies while iterating over the elements we have to store the mod of the prefix sum and whenever we encounter an existing mod we can return true

###### EXAMPLE ###############
### arr = [23,2,4,6,6], k= 7 ######
# idx     n       prefix_sum  dict key=(prefix_sum%k), value=current_element_idx
#                                 {0:-1}   # Initialization
# 0      23          23           {0:-1, 2:0}
# 1      2           25           {0:-1, 2:0, 4:1}
# 2      4           29           {0:-1, 2:0, 4:1, 1:2}
# 3      6           35           35%7 == 0, 0 was present in dict and idx - dict[0] > 1 ret True 
# 4      6       

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0:-1}
        sum = 0
        for i, num in enumerate(nums):
            sum+=num
            key = sum%k if k!=0 else sum
            if key in hashMap:
                if i - hashMap[key] > 1:
                    return True
            else:
                hashMap[key] = i
        return False