class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(n):
            res = 0
            for p in piles:
                res += ceil(p/n)
            return res
        
        l = 0
        r = max(piles) + 1
        
        while r > l + 1:
            mid = l + (r - l) // 2
            
            curTotal = helper(mid)
            
            if curTotal > h:
                l = mid
            else:
                r  = mid
        return r