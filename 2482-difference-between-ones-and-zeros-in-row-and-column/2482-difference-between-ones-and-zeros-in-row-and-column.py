class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        onesrow = [0] * len(grid)
        onescol = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                onesrow[i] += grid[i][j]
                onescol[j] += grid[i][j]
                
            
        for i in range(len(onesrow)):
            drow = []
            for j in range(len(onescol)):
                d = onesrow[i] + onescol[j] - ((len(onesrow)) - onesrow[i]) - ((len(onescol)) - onescol[j])
                drow.append(d)
            diff.append(drow)
        return diff
            
        
            