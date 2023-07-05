class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, l, prefix = 0, 0, 0
        for r, n in enumerate(nums):
            prefix += n
            while prefix < r-l:
                prefix -= nums[l]
                l += 1
            ans = max(ans, r-l)
        return ans