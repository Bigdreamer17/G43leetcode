class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(lis, index):
            if lis not in ans:
                ans.append(lis[:])
                
            if index >= len(nums):
                return 
            
            lis.append(nums[index])
            backtrack(lis, index + 1)
            lis.pop()
            
            
            backtrack(lis, index + 1)
        backtrack([], 0)
        return ans