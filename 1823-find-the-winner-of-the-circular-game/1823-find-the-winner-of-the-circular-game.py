class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Base case
            # size of our queue must be = 1
        if n == 1:
            return 1
        x = self.findTheWinner(n -1, k)
        y = (x + k) % n
        if y == 0:
            return n
        return y