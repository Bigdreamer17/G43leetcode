class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        x = max(nums)
        y = min(nums)
        score = (x - k) - (y + k)

        return max(0, score)