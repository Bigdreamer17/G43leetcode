class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        bucket = set(nums)
        for i in range(len(nums)):  
            j = nums[i] - diff
            k = diff + nums[i]
            if j in bucket and k in bucket:
                ans +=1
        return ans