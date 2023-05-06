class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * (1<<N)
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                if mask & (1<<j):
                    neib = dp[mask ^ (1<<j)]
                    dp[mask] = neib|nums[j]
        return dp.count(max(dp))