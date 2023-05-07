class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapify(nums)
        ans = set()
        while sum(nums) != 0:
            x = heappop(nums)
            if x == 0:
                continue
            ans.add(x)
        return len(ans)