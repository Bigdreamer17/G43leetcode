class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # try to make it O(1) space
        n = len(matrix)
        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))] 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
        
        return ans