class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = 1
        while ptr2 < len(nums):
            if nums[ptr1] == nums[ptr2]:
                nums[ptr1] = nums[ptr1] * 2
                nums[ptr2] = 0
            ptr1 += 1
            ptr2 += 1
        
        ptr3 = 0
        for i in range(len(nums)):
            if not nums[ptr3] and nums[i]:
                nums[ptr3], nums[i] = nums[i], nums[ptr3]
                ptr3 += 1
            elif nums[ptr3] != 0:
                ptr3 += 1
        return nums
        