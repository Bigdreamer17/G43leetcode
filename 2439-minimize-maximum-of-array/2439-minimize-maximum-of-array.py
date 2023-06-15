class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        summ = 0
        ans =  float("-inf")
        
        for i in range(len(nums)):
            summ += nums[i]
            ans = max(ans, ceil(summ / (i + 1)))
        return int(ans)