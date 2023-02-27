class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divcount = 0
        dictt = {0 : 1}
        running_sum = 0
        for i in nums:
            running_sum += i
            if running_sum % k in dictt:
                divcount += dictt[running_sum % k]
            dictt[running_sum % k] = dictt.get(running_sum % k, 0) + 1
        return divcount