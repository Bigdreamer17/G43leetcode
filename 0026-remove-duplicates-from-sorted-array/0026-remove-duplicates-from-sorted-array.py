class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        right = 0
        while left < len(nums):
            if nums[left] not in seen:
                seen.add(nums[left])
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                
            else:
                left += 1
                
        return right