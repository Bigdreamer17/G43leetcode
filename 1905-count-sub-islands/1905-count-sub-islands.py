class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Row, Col = len(grid1), len(grid1[0]) 
        visited = set()
        
        def dfs(row, col):
            if (row < 0 or col < 0 or row == Row or col == Col or grid2[row][col] == 0 or (row, col) in visited):
                return True
            
            visited.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False
                
            res = dfs(row - 1, col) and res
            res = dfs(row + 1, col) and res
            res = dfs(row , col - 1) and res
            res = dfs(row , col + 1) and res
            
            return res
        
        length = 0
        for r in range(Row):
            for c in range(Col):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    length += 1
                    
        return length 