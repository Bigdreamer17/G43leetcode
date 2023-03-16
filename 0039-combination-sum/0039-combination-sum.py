class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(lis, indx):
            # End Goal
            if sum(lis) == target:
               ans.append(lis[:])
               return 
            
            # Constaraint
            if sum(lis) > target:
                return
            
            for i in range(indx, len(candidates)):
                lis.append(candidates[i])
                backtracking(lis,i)
                lis.pop()
                
        backtracking([], 0)
        return ans