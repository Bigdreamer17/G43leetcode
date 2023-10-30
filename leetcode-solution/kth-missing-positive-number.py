class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        size = len(arr)
        left = 0
        right = size

        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return left + k