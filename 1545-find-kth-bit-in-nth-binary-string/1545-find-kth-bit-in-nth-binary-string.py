class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base Case = S1 = "0"
        # Recurssive r/ship =  Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
        # State = n - 1
        
        def kth(n, k):
            if n == 1:
                return 0
            
            length = pow(2, n - 1) - 1
            
            if k - length == 1:
                return 1
            
            if k <= length:
                return kth(n -1, k)
            else:
                return 1 - int(kth(n - 1, 2 * (length + 1) - k))
            
        return str(kth(n, k))