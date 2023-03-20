class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(lis, index):
            # Goal
            if index >= len(nums):
                ans.append(lis[:])
                return 
            
            # Pick move
            lis.append(nums[index])
            backtrack(lis, index + 1)
            lis.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            # Don't pick move 
            backtrack(lis, index + 1)
            
        backtrack([], 0)
        
        return ans