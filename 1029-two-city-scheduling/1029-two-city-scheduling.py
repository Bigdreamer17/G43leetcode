class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        size = len(costs)
        costs.sort(key=lambda x:x[0] - x[1])
        print(costs)
        ans = 0
        for i in range(size):
            if i < size // 2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]
        return ans