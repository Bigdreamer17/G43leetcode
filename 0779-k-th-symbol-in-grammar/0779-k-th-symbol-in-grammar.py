class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base Case = one = 0
        # Case = n - 1
        # recuersive relation = 
        def kth(n, k):
            if n == 1:
                return "0"
            
            if k <= 2 ** (n - 2):
                return kth(n-1, k)
            else:
                return 1 - int(kth(n-1, k -  pow(2, n - 2)))
        return int(kth(n, k))