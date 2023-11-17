class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for j in range(1, numRows):
            prev = triangle[-1]
            triangle.append([1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1])
            
        return triangle