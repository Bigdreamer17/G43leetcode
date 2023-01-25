class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = ceil(sqrt(c))
        left = 0
        while left <= right:
            if right ** 2 + left ** 2 > c:
                right -= 1
            if right ** 2 + left ** 2 < c:
                left += 1
            else:
                return True
        return False
        
        
            