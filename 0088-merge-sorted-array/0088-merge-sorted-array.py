class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        compare each element from the start and place it in nums1 if and only if the num2[i] >= nums[i]
        """
        i = (m + n)- 1
        ptr1 = m - 1
        ptr2 = n - 1 
        while ptr2 >= 0:
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
                i -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
                i -= 1