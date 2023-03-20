class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping ={
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        ans = []
        
        def backtrack(index, curstr):
            if len(curstr) == len(digits):
                ans.append(curstr)
                return 
            
            for c in mapping[digits[index]]:
                backtrack(index + 1, curstr + c)
        if digits:
            backtrack(0, "")
        return ans