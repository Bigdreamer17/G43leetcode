class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count = 0
        valid = 2 ** 32 - 1
        
        for i in range(len(nums)):
            valid  &= nums[i]
            
        if valid > 0:
            return 1
        
        valid = 2 ** 32 - 1
        for i in range(len(nums)):
            valid &= nums[i]
            if valid == 0:
                count += 1
                valid = 2 ** 32 - 1
        return count