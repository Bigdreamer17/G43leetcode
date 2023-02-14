class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        numbers = set([i for i in range(1,10)])
        def check(i, j):
            if numbers != set([grid[i+di][j+dj] for di in range(3) for dj in range(3)]):
                return False
            s = sum(grid[i][j+k] for k in range(3))
            for di in range(3):
                if s != sum(grid[i+di][j+k] for k in range(3)): return False
            for dj in range(3):
                if s != sum(grid[i+k][j+dj] for k in range(3)): return False
            if s != sum(grid[i+k][j+k] for k in range(3)): return False
            if s != sum(grid[i+k][j+2-k] for k in range(3)): return False
            return True
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m-2):
            for j in range(n-2):
                res += check(i,j)
        return res