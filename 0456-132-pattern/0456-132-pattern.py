class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monostack = []
        minn = -inf
        for i in nums[::-1]:
            if i < minn:
                return True
            while monostack and monostack[-1] < i:
                minn = monostack.pop()
            monostack.append(i)
        return False