class Solution:
    def dp(self, triangle, index):
         
        
        for j in range(len(triangle[index])):
            triangle[index][j] += min(triangle[index + 1][j], triangle[index + 1][j + 1])
            
        if index == 0:
            return triangle[0][0]
        
        return self.dp(triangle, index - 1)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        
        return self.dp(triangle, len(triangle) - 2)