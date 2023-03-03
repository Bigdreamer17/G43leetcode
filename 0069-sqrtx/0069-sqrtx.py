class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low =  mid + 1
        return low - 1
        