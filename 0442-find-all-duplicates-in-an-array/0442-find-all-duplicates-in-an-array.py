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
    # i=0
    # while i<len(nums):
    #     idx=nums[i]-1
    #     if nums[i]!=i+1 and nums[idx]!=nums[i]:
    #         nums[i],nums[idx]=nums[idx],nums[i]
    #     else:
    #         i+=1
    # for i in range(len(nums)):
    #     if nums[i]!=i+1:
    #         yield nums[i]