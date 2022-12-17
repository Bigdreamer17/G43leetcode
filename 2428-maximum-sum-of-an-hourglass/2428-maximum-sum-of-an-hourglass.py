class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        k = 3
        m , n = len(grid), len(grid[0])
        
        res = 0
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                s = 0
                for row_index in range(i, i + 3):
                    s += sum(grid[row_index][j: j+3])
                s -= grid[i+1][j] + grid[i+1][j+2]
                res = max(res, s)
        return res