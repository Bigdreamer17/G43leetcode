class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        for key, value in dictionary.items():
            if value > 1:
                return key