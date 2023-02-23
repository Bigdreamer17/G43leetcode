class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forwardsum = 0
        totalsum = sum(nums)
        
        for indx, i in enumerate(nums):
            if forwardsum == totalsum - i:
                return indx
            forwardsum += i 
            totalsum -= i        
        return -1