class Solution:
    def minPartitions(self, n: str) -> int:
        ans = float('-inf')
        for i in n:
            ans = max(ans, int(i))
        return ans