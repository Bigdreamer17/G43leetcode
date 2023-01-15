class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split(" ")
        size = len(ans)
        for index in range(size):
            if ans[-1] == '':
                ans.pop()
            else:
                return len(ans[-1])
                break