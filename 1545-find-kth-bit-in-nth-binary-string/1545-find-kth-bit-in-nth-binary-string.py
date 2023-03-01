class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base Case = S1 = "0"
        # Recurssive r/ship =  Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
        # State = n - 1
        
        def bit(n):
            if n == 1:
                return "0"
            
            prev = bit(n- 1)
            invert = ""
            for i in prev:
                if i == '0':
                    invert += '1'
                else:
                    invert += '0'
            return prev + '1' + invert[::-1]
        
        
        s = bit(n)
        return s[k - 1]
        