class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        for i, j in enumerate(nums):
            freq[j].append(i)

        nums_degree = max([len(i) for i in freq.values()])

        answer = len(nums)
        for value in freq.values():
            if len(value) == nums_degree:
                answer = min(answer, value[-1] - value[0] + 1)
        return answer