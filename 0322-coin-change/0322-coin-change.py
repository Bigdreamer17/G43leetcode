class Solution:
    # def solve(self, coins, amount):
    #     answer = float('inf')
    #     for c in coins:
    #         answer  = min(answer, self.solve(coins, amount - c))
    #     return answer
    def coinChange(self, coins: List[int], amount: int) -> int:
        # self.solve(coins, amount)
        
        #Bottom-up approach
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for am in range(1, amount + 1):
            for c in coins:
                if am - c >= 0:
                    dp[am] = min(dp[am], dp[am - c] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
        