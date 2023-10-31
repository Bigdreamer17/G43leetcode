class Solution:
    def dfs(self, graph, s, d):
        visited = set()
        stack = [(s, 1.0)]
        if s not in graph or d not in graph:
            return -1
        
        while stack:
            (vertex, product) = stack.pop()
            if vertex == d:
                return product
            elif vertex not in visited:
                visited.add(vertex)
                for neighbour, weight in graph[vertex]:
                    if neighbour not in visited:
                        stack.append((neighbour, product * weight))
        return -1
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        result = []

        for e in range(len(equations)):
            graph[equations[e][0]].append([equations[e][1], values[e]])
            graph[equations[e][1]].append([equations[e][0], 1 / values[e]])

        for query in queries:
            value = self.dfs(graph, query[0], query[1])
            result.append(value)
        return result