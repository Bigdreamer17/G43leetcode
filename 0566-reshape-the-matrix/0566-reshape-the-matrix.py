class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_list = []
        matrix = []

        for sublist in mat:
            for item in sublist:
                flat_list.append(item)

        if len(flat_list) != r * c:
            return mat
        else:
            for i in range(0,len(flat_list),c):
                matrix.append(flat_list[i:i+c])
            return matrix