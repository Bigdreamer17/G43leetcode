class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, j in enumerate(nums):
            m = target - j 
            if m in dictionary:
                return [dictionary[m], i]
            dictionary[j] = i