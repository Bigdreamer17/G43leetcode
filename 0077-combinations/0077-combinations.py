class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        integers = []
        # building our integer array
        for i in range(1, n + 1):
            integers.append(i)
        
        def backtrack(lis, index):
            # Goal
            if len(lis) == k:
                ans.append(lis[:])
                return
            # Constraints
            if index >= len(integers):
                return 
            if len(lis) > k:
                return
            # Choices
                # Pick move
            lis.append(integers[index])
            backtrack(lis, index + 1)
            lis.pop()
            
            # Don't pick move
            backtrack(lis, index + 1)
        backtrack([], 0)
        return ans
            