class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(rowIndex):
            if rowIndex == 0:
                return [1]
            row = [1] * (rowIndex + 1)
            prev = pascal(rowIndex - 1)
            
            for i in range(1,len(prev)):
                row[i] = prev[i] + prev[i - 1]
            
            return row
        return pascal(rowIndex)
        