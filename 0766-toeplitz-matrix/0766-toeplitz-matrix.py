class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                    if row - col not in dic:
                        dic[row - col] = matrix[row][col]
                    elif dic[row - col] != matrix[row][col]:
                        return False
        return True