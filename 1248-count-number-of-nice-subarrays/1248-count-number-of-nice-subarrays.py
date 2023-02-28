class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
        
    def atMost(self, nums: List[int], k: int) -> int:
        countOfSubarrays = 0
        
        i,j = 0,0
        n = len(nums)
        
        odd = 0
        
        while j < n:
            if nums[j] % 2 != 0 : odd += 1
                
            if odd > k:
                while odd > k:
                    if nums[i] % 2 != 0: odd -= 1
                    i += 1
            
            countOfSubarrays += j - i + 1
            j += 1
        
        return countOfSubarrays