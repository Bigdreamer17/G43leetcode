class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for col in range(len(matrix[0])):
            for row in range(col + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        
        for i in matrix:
            i.reverse()
        # for row in range(size):
        #     for col in range(row + 1, size):
        #         matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row] 