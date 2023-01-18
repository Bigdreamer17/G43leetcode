class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        if size < 3:
            return False
        left_ptr = 0
        right_ptr = size - 1
        peak = max(arr)
        while left_ptr + 1 < size - 1 and arr[left_ptr] < arr[left_ptr + 1]:
            left_ptr += 1
        if left_ptr == 0 or left_ptr == right_ptr:
            return False
        while right_ptr - 1 < size - 1 and arr[right_ptr] < arr[right_ptr - 1]:
            right_ptr -= 1
        
        return left_ptr == right_ptr