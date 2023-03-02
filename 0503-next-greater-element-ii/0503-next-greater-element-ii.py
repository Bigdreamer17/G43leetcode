class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        decresing_stack = []
        ans = [-1] * len(nums)
        
        # Traverse 2 to simulate the circular aspect
        for _ in range(2):
            for indx, val in enumerate(nums):
                while decresing_stack and val > nums[decresing_stack[-1]]:
                        ans[decresing_stack.pop()] = val
                decresing_stack.append(indx)
        return ans
                    