class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        integers = [] 
        for i in range(1, n + 1):
            integers.append(i)
        
        def backtrack(lis, index):
            if len(lis) == k:
                ans.append(lis[:])
                return
            
            if index >= len(integers):
                return 
            if len(lis) > k:
                return
            
            lis.append(integers[index])
            backtrack(lis, index + 1)
            lis.pop()
            
            backtrack(lis, index + 1)
        backtrack([], 0)
        return ans
            