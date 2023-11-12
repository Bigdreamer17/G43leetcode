class StockSpanner:

    def __init__(self):
        self.monostack = []
        self.stack = []
    def next(self, price: int) -> int:
        if not self.monostack:
            self.monostack.append(price)
            self.stack.append(1)
            return 1
        
        counter = 1
        while self.monostack:
            if self.monostack[-1] <= price:
                counter += self.stack.pop()
                self.monostack.pop()
            else:
                break
        self.monostack.append(price)
        self.stack.append(counter)
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)