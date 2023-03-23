class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort it and return -k 
        def quicksort(nums, start, end):
            if end - start <= 0:
                return

            pivot = nums[start]
            write = start + 1

            for read in range(start + 1, end + 1):
                if nums[read] <=  pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
            nums[start], nums[write - 1] = nums[write - 1], nums[start]
            quicksort(nums, start, write - 2)
            quicksort(nums, write, end)
            
        quicksort(nums, 0, len(nums) - 1)
        return nums[-k]
        