class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tar = []
        for i in matrix:
            if i[0] <= target:
                tar = i
        return target in set(tar)