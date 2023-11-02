class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        pairs  = 0
        for val in freq.values():
            pairs += val * (val - 1) // 2
        return pairs