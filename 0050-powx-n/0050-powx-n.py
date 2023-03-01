class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return x
        return x * pow(x, n - 1)