class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Row = len(image)
        Col = len(image[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visted = [[0 for i in range(Col)] for j in range(Row)]
        
        def inbound(row, col):
            return (0 <= row < Row and 0 <= col < Col)
        
        def dfs(start_pos, row, col):
            
            visted[row][col] = True
            
            for row_change , col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visted[new_row][new_col]:
                    if image[new_row][new_col] == start_pos:
                        image[new_row][new_col] = color
                        
                        dfs(start_pos,new_row, new_col)
        
        dfs(image[sr][sc],sr,sc)
        image[sr][sc] = color
        
        return image