class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while(i < n):
            correctIdx = nums[i] - 1

            if nums[i] != nums[correctIdx] and nums[i] != i + 1:
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i += 1
        
        return nums[-1]