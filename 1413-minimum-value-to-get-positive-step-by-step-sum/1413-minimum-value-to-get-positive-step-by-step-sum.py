class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])

        min_prefix = min(prefix)

        if min_prefix < 0:
            return 1 - (min_prefix)
        else :
            return 1