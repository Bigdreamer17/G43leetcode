class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_reversed = []
        
        for i in nums:
            reverse = str(i)[::-1]
            nums_reversed.append(int(reverse))
        
        nums += nums_reversed
        reversed_list = set(nums)
        
        return len(reversed_list)