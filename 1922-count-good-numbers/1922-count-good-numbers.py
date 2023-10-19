class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ans = pow(20, n // 2, mod)
        if n % 2 == 0:
            return ans
        else:
            return ans * 5 % mod
        