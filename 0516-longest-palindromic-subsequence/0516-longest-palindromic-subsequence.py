class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(1, n):
            for j in range(0, n -i):
                k = i + j
                if s[j] == s[k]:
                    dp[j][k] = 2 + dp[j + 1][k - 1]
                else:
                    dp[j][k] = max(dp[j + 1][k],dp[j][k - 1])
                    
        return dp[0][n - 1]