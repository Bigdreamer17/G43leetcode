class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        x = (num - 3) // 3
        if isinstance(x, int) and (x + x + 1 + x + 2) == num:
            ans.append(x)
            ans.append(x + 1)
            ans.append(x + 2)
            return ans
        else:
            return ans
         