class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0] * 2055

        for start, end in logs:
            for i in range(start, end):
                count[i] += 1

        max_pop = max(count)
        for index in range((len(count))):
            if count[index] == max_pop:
                return index
        return -1