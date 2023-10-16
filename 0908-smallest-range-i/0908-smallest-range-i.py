class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_score = max(0, max(nums) - min(nums) - 2*k)       
        return min_score 