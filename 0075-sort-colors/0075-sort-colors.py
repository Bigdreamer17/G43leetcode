class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            for j in range(i, size):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]