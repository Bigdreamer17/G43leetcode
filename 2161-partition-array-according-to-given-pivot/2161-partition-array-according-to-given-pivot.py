class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        equal = []
        for i in nums:
            if i < pivot:
                less.append(i)
            if i > pivot:
                greater.append(i)
            if i == pivot:
                equal.append(i)
        nums = less + equal + greater
        return nums