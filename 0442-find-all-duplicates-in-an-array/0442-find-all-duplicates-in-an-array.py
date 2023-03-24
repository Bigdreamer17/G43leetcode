class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while(i < n):
            correctIdx = nums[i] - 1

            if nums[i] != nums[correctIdx] and nums[i] != i + 1:
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i += 1
                
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                    ans.append(nums[i])
        return ans