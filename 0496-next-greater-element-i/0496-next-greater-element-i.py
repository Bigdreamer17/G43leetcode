class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashh = {}
        ans  = []
        for i in nums2:
            while stack and stack[-1] < i:
                var = stack.pop()
                hashh[var] = i
            stack.append(i)
        for i in nums1:
            if i in hashh:
                ans.append(hashh[i])
            else:
                ans.append(-1)
        return ans
            