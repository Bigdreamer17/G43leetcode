class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowLimits, colLimits = [0] * rows, [0] * cols
        sol = 0

        for row in range(rows):
            for col in range(cols):
                rowLimits[row] = max(rowLimits[row], grid[row][col])
                colLimits[col] = max(colLimits[col], grid[row][col])

        for row in range(rows):
            for col in range(cols):
                sol += (min(rowLimits[row], colLimits[col]) - grid[row][col])
        
        return sol