class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # nums.sort()
        if len(nums) <= 3:
            return 0 
        nums.sort()
        min_Diff = float('inf')
        for i in range(4):
                min_Diff = min(min_Diff, nums[i - 4] - nums[i])
        
        return min_Diff