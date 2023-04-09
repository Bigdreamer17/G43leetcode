class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()

        for i in range(len(nums)):
            start = 2
            while start <= nums[i]:
                while nums[i]% start == 0:
                    s.add(start)
                    nums[i] = nums[i] //start
                start +=1

        return len(s)