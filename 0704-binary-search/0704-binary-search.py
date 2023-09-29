class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(array, x, low, high):
            while low <= high:

                mid = low + (high - low)//2

                if array[mid] == x:
                    return mid

                elif array[mid] < x:
                    low = mid + 1

                else:
                    high = mid - 1
                
            return -1
        
        return binarySearch(nums, target, 0 , len(nums) - 1)