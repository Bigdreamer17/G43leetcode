class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for indx, value in enumerate(nums):
            if value == target:
                ans.append(indx)
        return ans
        