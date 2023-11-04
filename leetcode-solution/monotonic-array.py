class Solution:
    def Increasing(self, nums):
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
        return stack == sorted(nums)
    def Decreasing(self, nums):
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        return stack == sorted(nums, reverse = True)
    def isMonotonic(self, nums: List[int]) -> bool:
        if self.Increasing(nums) or self.Decreasing(nums):
            return True
        return False