class Solution:
    def balancedStringSplit(self, s: str) -> int:
        variable = 0
        ans = 0
        for letter in s:
            if letter == 'L':
                variable += 1
            else:
                variable -= 1
            if variable == 0:
                ans += 1
        return ans