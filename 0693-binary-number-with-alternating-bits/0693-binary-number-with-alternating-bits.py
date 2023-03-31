class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shift = n >> 1
        n = n ^ shift
        return (n & n + 1) == 0