class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def Backtrack(nums, result = [],permtuation = []):
            if not nums:
                result.append(permtuation[::])
                
    
            for i in range(len(nums)):
                New_number = nums[:i] + nums[i+1:]
                permtuation.append(nums[i])
                
                Backtrack(New_number, result,permtuation)
                permtuation.pop()
                
            return result
        
        return Backtrack(nums)