class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        
        pt1 , pt2 = 0 , 0
        while pt1 < len(nums) and pt2 < len(nums):
            if (pt2 + 1) < len(nums) and nums[pt2] + 1 == nums[pt2 + 1]:
                pt2 = pt2 + 1
            else:
                if nums[pt1] == nums[pt2]:
                    ans.append(str(nums[pt1]))
                    pt1 = pt1 + 1
                    pt2 = pt2 + 1
                else:
                    ans.append(str(nums[pt1]) + '->' + str(nums[pt2]))
                    pt2 = pt2 + 1
                    pt1 = pt2
                    
                    
        return ans