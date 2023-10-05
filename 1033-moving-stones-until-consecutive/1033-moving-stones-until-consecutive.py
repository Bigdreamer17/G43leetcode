class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c=sorted([a,b,c])
        minimum = 0
        maximum = c - a -2
        if a + 1 == b or b + 1 == c:
            minimum=1
        elif a+2 == b or b+2 == c:
            minimum = 1
        else:
            minimum = 2
        if maximum == 0:
            minimum = 0
        return [minimum, maximum]