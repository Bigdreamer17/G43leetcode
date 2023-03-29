class Solution:
    def reverseBits(self, n: int) -> int:
        pos = 32 - 1
        
        reverse = 0
        
        while pos >= 0 and n:
            if n & 1:
                reverse = reverse | (1 << pos)
                
            n >>= 1
            pos -= 1
            
        return reverse