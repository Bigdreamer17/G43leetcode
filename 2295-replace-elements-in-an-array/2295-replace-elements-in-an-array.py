class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dic={}
        for i in range(len(nums)):
            nums_dic[nums[i]] = i
        for index, value in operations:
            curr = nums_dic[index]
            nums[curr] = value
            nums_dic[value] = curr
                
        return nums