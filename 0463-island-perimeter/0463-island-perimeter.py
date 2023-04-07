class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for r in range(row):
            for c in range(col):
                count = 0
                if grid[r][c] == 1:
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        count += 1
                    if r + 1 < row and grid[r + 1][c] == 1:
                        count += 1
                        
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        count += 1
                    if c + 1 < col and grid[r][c + 1] == 1:
                        count += 1
                        
                    perimeter += (4 - count)
        return perimeter