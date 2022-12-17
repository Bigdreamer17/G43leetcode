class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # creating MaxLocal
        maxLocal = [[0] * (n-2) for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                maxLocal[i][j] = max(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))
        return maxLocal