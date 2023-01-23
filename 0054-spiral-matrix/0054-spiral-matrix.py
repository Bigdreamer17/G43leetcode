class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nr, nc = len(matrix), len(matrix[0])
        rs = cs = 0
        r = c = 0
        turn = 0
        ans = []
        while nr > rs and nc > cs:
            if turn % 4 == 0:  # col+
                for ci in range(cs, nc):
                    ans.append(matrix[r][ci])
                c = ci  # standing in this column
                rs += 1  # a row is eliminated at the top
            elif turn % 4 == 1:  # row+
                for ri in range(rs, nr):
                    ans.append(matrix[ri][c])
                r = ri  # standing in this row
                nc -= 1  # a column is eliminated on the right
            elif turn % 4 == 2:  # col-
                for ci in range(nc-1, cs-1, -1):
                    ans.append(matrix[r][ci])
                c = ci  # standing in this column
                nr -= 1  # a row is eliminated at the bottom
            elif turn % 4 == 3:  # row-
                for ri in range(nr-1, rs-1, -1):
                    ans.append(matrix[ri][c])
                r = ri  # standing in this row
                cs += 1  # a column is eliminated on the left
            turn += 1

        return ans