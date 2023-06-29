class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = { 0 : 1 }
        
        for total in range(1, target + 1):
            cache[total] = 0
            for num in nums:
                cache[total] += cache.get(total - num, 0)
        return cache[total]