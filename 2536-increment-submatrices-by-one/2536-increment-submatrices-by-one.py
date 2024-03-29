class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n + 1)] for __ in range(n)]
        for query in queries:
            r1, c1, r2, c2 = query
            for i in range(r1, r2 + 1):
                mat[i][c1] += 1
                mat[i][c2 + 1] -= 1
        
        for i in range(n):
            for j in range(1, n + 1):
                mat[i][j] += mat[i][j - 1]
        
        for i in range(n):
            mat[i] = mat[i][:n]
        
        return mat