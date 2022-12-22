class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for value in d.values():
            ans += (value * (value - 1)) // 2
        return ans