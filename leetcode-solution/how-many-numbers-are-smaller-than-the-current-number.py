class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy = sorted(nums)
        ans = []
        freq = {}

        for i in range(len(nums)):
            if copy[i] not in freq:
                freq[copy[i]] = i

        for i in nums:
            ans.append(freq[i])
        return ans