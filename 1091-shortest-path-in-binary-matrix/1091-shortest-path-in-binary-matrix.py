class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque([(0,0,1)]) #row, col, length
        visit = set((0,0))

        directions = [[0,1], [1,0], [0, -1], [-1, 0], [1,1], [-1,-1], [1,-1], [-1,1]]

        while q:
            r,c,length = q.popleft()

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
                continue

            if r == rows - 1 and c == cols - 1:
                return length

            for horizontal, vertical in directions:
                nr = r + horizontal
                nc = c + vertical

                if (nr,nc) not in visit:
                    q.append((nr,nc,length+1))
                    visit.add((nr,nc))


        
        return -1