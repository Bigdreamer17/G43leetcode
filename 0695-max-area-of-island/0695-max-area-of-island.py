class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area
    
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
             return 0
        
        grid[i][j] = 0
        count = 1
        
        count += self.dfs(grid, i, j+1)
        count += self.dfs(grid, i, j-1)
        count += self.dfs(grid, i+1, j)
        count += self.dfs(grid, i-1, j)
        
        return count