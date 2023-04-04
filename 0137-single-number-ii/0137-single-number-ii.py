class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        mask = 1
        while mask < 2**32:
            ones = 0
            for i in nums:
                ones += (i & mask)
            if ones % 3 != 0:
                single |= mask
            
            mask <<= 1
            
            if single & (1 << 31):
                return (2 ** 32 - single) * -1
        return single