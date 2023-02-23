class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
            row, col = len(matrix), len(matrix[0])
            
            self.presum = [[0] * (col + 1) for i in range(row + 1)]
            
            for r in range(row):
                prefix = 0
                for c in range(col):
                    prefix += matrix[r][c]
                    above = self.presum[r][c + 1]
                    self.presum[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        A, B, C, D = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottomright = self.presum[C][D]
        bottomleft = self.presum[C][B - 1]
        aboveleft = self.presum[A - 1][B - 1]
        aboveright = self.presum[A - 1][D]
        
        return bottomright + aboveleft - bottomleft - aboveright

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)