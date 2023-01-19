class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        count = 0
        ans = []
        for i in nums:
            for j in temp:
                if i > j:
                    count += 1
            ans.append(count)
            count = 0
        return ans
                