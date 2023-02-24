class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []

    def push(self, val: int) -> None:
        # self.minn = min(self.minn, val)
        self.stack.append(val)
        val = min(val, self.minn[-1] if self.minn else val)
        self.minn.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()
        # self.minn = min(self.minn, val)
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()