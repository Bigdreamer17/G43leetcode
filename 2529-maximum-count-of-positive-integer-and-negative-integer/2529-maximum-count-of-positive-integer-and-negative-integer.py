class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binarySearch(nums,target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1 
                else:
                    right = mid - 1
            return left
        
        return max(binarySearch(nums,0), len(nums) - binarySearch(nums,1))