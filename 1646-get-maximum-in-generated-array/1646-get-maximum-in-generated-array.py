class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        array = [0] * (n + 1)
        array[1] = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                array[i] = array[i // 2]
            else:
                array[i] = array[i // 2] + array[(i // 2) + 1]
        return max(array)            