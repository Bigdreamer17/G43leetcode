class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        size = len(nums)
        
        while i < size:
            correctIndex = nums[i] - 1
            
            if nums[i] != nums[correctIndex] and nums[i] != i + 1:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i +1]
                