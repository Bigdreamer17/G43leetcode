class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        length = float('inf')
        summ = 0
        
        while right < len(nums):
            summ += nums[right]
            while summ >= target:
                summ -= nums[left]
                length = min(length, right - left + 1)
                left += 1
            right += 1
        
        if length == float('inf'):
            return 0
        else:
            return length