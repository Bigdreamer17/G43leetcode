class Solution:
    def __init__(self):
        self.cache = {}
        
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n not in self.cache.keys():
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]