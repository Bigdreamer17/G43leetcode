class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        numbers = []
        
        for i in range(1,10):
            numbers.append(i)
        
        def backtrack(lis, index):
            # Goal
            if len(lis) == k and sum(lis) == n:
                ans.append(lis[:])
                return
            
            # Constaraints
            if index >= len(numbers):
                return
            
            
            # Pick Move
            lis.append(numbers[index])
            backtrack(lis, index + 1)
            lis.pop()
            
            # Don't Pick move
            backtrack(lis, index + 1)
        backtrack([], 0)
        return ans