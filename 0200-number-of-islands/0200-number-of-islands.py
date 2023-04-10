class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            # base case
            visited[row][col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == "1":
                    dfs(grid, visited, new_row, new_col)
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not visited[row][col]:
                    count += 1
                    dfs(grid, visited, row, col)
        return count
        
#         count = 0
#         def dfs(grid, r, c, visted):
#             nonlocal count 
#             Row, Col = len(grid), len(grid[0])
#             # Constraints
#             if (min(r,c) < 0 or r == Row or c == Col or (r ,c) in visted or grid[r][c] == "0"):
#                 return 0
#             if r == Row - 1 and c == Col - 1:
#                 return 1
#             if grid[r][c] == "1" and (r,c) not in visted:
#                 visted.add((r, c))
            
            
            
#             count += dfs(grid, r + 1, c, visted)
#             count += dfs(grid, r - 1, c, visted)
#             count += dfs(grid, r, c + 1, visted)
#             count += dfs(grid, r, c - 1, visted)
            
#             visted.remove((r,c))
#             return count 
#         return dfs(grid, 0 , 0, set())