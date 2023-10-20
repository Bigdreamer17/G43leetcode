class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        dp_up = [0] * n
        dp_down = [0] * n
        
        team = 0
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    dp_up[i] += 1
                    team += dp_up[j]
                else:
                    dp_down[i] += 1
                    team += dp_down[j]
                    
        return team