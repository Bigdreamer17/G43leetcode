class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        hashmap = Counter()
        for num in deliciousness:
            for i in range(22): 
                result += hashmap[2**i-num]
            hashmap[num] += 1
        return result % ((10 ** 9) + 7)