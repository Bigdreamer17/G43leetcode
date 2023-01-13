class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # m = row , n = col
        answer = [[0] * n for _ in range(m)]
        arr_len = len(original)
        index = 0
        if m * n != arr_len:
            return []
        for row in range(m):
            for col in range(n):
                answer[row][col] = original[index]
                index += 1
        return answer