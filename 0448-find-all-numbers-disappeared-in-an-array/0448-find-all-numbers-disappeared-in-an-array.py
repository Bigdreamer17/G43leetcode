class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while(i < n):
            correctIdx = nums[i] - 1

            if (nums[i] != nums[correctIdx]):
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i += 1
                
        ans = []
        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(i + 1)

        return ans