class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)
        indegree = [0] * n
        outdegree = [0] * n
        for t in trust:
            graph[t[0]] = t[1]
            indegree[t[1] - 1] += 1
            outdegree[t[0] - 1] += 1
        
        for i in range(n):
            if indegree[i] - outdegree[i] == n - 1:
                return i + 1
        return -1
        