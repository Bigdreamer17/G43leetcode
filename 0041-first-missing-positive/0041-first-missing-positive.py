class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present_values = set()

        for v in nums:
            if v > 0:
                present_values.add(v)
                
        cur = 1
        while cur in present_values:
            cur += 1

        return cur