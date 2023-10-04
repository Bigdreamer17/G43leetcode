class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum  = [0 for _ in range(n)]
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            
        left_sums = [0 for _ in range(n)]
        right_sums = [0 for _ in range(n)]
        ans = [0 for _ in range(n)]        
        
        for i in range(n):
            total_sum = prefix_sum[n - 1]
            
            left_sums[i] = prefix_sum[i - 1] if i > 0 else 0
            right_sums[i] = total_sum - prefix_sum[i]
            ans[i] = abs(left_sums[i] - right_sums[i])
            
        return ans