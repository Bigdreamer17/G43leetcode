class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        l = r = 0

        while l < len(nums):
            if nums[l] not in visited:
                visited.add(nums[l])
                nums[l], nums[r] = nums[r], nums[l]
                r += 1

            else:
                l += 1
        return r 