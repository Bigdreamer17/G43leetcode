class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def GCD(a, b):
            while b:
                a , b = b, a % b
            return a
        
        count = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = GCD(cur, nums[j])
                if cur == k:
                    count += 1
                elif cur % k !=0 and cur < k:
                    break
        return count