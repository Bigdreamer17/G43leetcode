class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def helper(threshold): 
            return sum((num -1) // threshold + 1 for num in nums)
        
        l, r = 1, max(nums)
        while l <= r:
            mid = l + (r -l) // 2
            if helper(mid) <= threshold:
                r =  mid - 1
            else:
                l = mid + 1
        return l