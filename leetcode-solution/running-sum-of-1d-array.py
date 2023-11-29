class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        for num in nums:
            if len(prefix) != 0:
                prefix.append(num + prefix[-1])
            else:
                prefix.append(num)
        return prefix