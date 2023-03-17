class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(lis, index):
            # End Goal
            if sum(lis) == target:
                ans.append(lis[:]) # LIS[:] Same as i for i in lis
                return 
            
            # Constaraint
            if sum(lis) > target:
                return
            if index >= len(candidates):
                return
            # Pick stay
            lis.append(candidates[index])
            backtracking(lis, index)
            lis.pop()
            # Dont pick move
            backtracking(lis, index + 1)
        backtracking([], 0)
        return ans