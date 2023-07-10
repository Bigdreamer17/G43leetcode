class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        graph = defaultdict(list)
        ans = []
        for i in edges:
            graph[i[0]].append(i[1])
            indegree[i[1]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                ans.append(i)
        return ans