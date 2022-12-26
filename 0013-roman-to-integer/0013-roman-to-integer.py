class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_numbers ={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans = 0
        
        for i in range(len(s)- 1):
            if Roman_numbers[s[i]] < Roman_numbers[s[i + 1]]:
                ans -= Roman_numbers[s[i]] 
            else:
                ans += Roman_numbers[s[i]]
        
        return ans + Roman_numbers[s[-1]]
        
        