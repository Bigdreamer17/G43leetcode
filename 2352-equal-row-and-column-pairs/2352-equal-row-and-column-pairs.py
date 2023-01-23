class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        
        for row in range(n):
            for col in range(n):
                has_found = True
                
                for i in range(n):
                    if grid[row][i] != grid[i][col]:
                        has_found = False
                        break
                    
                if has_found:
                    ans += 1
					
        return ans
                    