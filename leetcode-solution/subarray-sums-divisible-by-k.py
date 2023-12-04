class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rs = ans = 0
        freq = {0: 1}

        for num in nums:
            rs += num
            key = rs % k

            if key in freq:
                ans += freq[key]
                freq[key] += 1
            else:
                freq[key] = 1
        return ans