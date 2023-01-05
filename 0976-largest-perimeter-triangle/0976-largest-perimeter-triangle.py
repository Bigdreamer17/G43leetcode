class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        list_size = len(nums) 
        for i in range(list_size - 3,-1,-1):
            perimeter = nums[i] + nums[i + 1] + nums[i + 2]
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return perimeter
        return 0