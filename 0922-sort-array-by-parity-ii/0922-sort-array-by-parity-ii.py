class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        iEven = 0
        iOdd = 1
        while True:
            while iEven < n and nums[iEven] % 2 == 0:
                iEven += 2
            while iOdd < n and nums[iOdd] % 2 == 1:
                iOdd += 2
            if iEven >= n or iOdd >= n:
                break

            nums[iEven], nums[iOdd] = nums[iOdd], nums[iEven]
            iEven += 2
            iOdd += 2
        return nums