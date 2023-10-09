class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, 0 
        totalDistinct = len(set(nums)) 
        hm = defaultdict(int)
        ans = 0 
        
        while R < n: 
            cur = nums[R]
            hm[cur] += 1 
            if len(hm.keys()) == totalDistinct: 
               
                ans += abs(n - R)
                hm[nums[L]] -= 1 
                if hm[nums[L]] == 0:
                    hm.pop(nums[L])
                L += 1 
              
                while L < R and len(hm.keys()) == totalDistinct: 
                    ans += abs(n - R)
                    hm[nums[L]] -= 1 
                    if hm[nums[L]] == 0:
                        hm.pop(nums[L])
                    L += 1 
                R += 1 
            else:
                R += 1 
        return ans 

