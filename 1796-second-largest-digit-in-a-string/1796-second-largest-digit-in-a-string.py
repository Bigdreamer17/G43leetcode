class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        
        for i in s:
            if i.isnumeric():
                digits.append(int(i))
                
        
        
        if len(set(digits)) < 2:
            return -1
        else:
            digits = list(set(digits))
            digits.sort()
            return digits[len(digits) - 2]