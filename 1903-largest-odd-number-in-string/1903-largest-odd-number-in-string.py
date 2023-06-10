class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        if int(num[-1]) % 2 != 0:
            return num
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) == 0 or int(num[i]) % 2 == 0:
                continue
            else:
                ans += num[:i+1]
                break
        return ans