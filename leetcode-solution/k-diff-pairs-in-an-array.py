class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0

        if k == 0:
            for i in freq.values():
                if i > 1:
                    ans += 1
            return ans
        
        for key in freq.keys():
            if key + k in freq:
                ans += 1
        return ans
