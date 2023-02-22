class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right  = 0
        summ = 0
        window = float('inf')
        
        while right < len(nums):
            summ += nums[right]
            while summ >= target:
                summ -= nums[left]
                window = min(window, right - left + 1)
                left += 1
            right += 1
        
        if window == float('inf'):
            return 0
        
        return window