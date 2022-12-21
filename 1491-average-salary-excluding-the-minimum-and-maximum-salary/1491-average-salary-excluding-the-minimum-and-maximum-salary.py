class Solution:
    def average(self, salary: List[int]) -> float:
        summ = sum(salary)
        minn = min(salary)
        maxx = max(salary)
        summ -= (minn + maxx)
        n = len(salary) - 2
        return summ / n