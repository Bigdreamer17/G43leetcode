class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        EvenSum = sum(x for x in nums if x % 2 == 0)
        for j, k in queries:
            if nums[k] % 2 == 0:
                EvenSum -= nums[k]
            nums[k] += j
            if nums[k] % 2 == 0:
                EvenSum += nums[k]
            answer.append(EvenSum)
        return answer