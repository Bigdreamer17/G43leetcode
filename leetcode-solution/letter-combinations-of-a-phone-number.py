class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",
        }

        ans  = []

        def backtrack(idx, curstr):
            if len(curstr) == len(digits):
                ans.append(curstr)
                return

            for chr in mappings[digits[idx]]:
                backtrack(idx + 1, curstr + chr )
        if digits:
            backtrack(0, "")
        return ans 