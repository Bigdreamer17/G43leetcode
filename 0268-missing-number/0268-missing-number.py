class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def cyclic_sort(nums):
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] < n and i != nums[i]:
                    swap(nums, i, nums[i])
                else:
                    i+= 1
        
        cyclic_sort(nums)
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)