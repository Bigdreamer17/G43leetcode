class Solution:
    def dfs(self, graph, source, destination):
        visited = set()
        stack = [(source, 1.0)]
        if source not in graph or destination not in graph:
            return -1

        while stack:
            (vertex, product) = stack.pop()
            if vertex == destination:
                return product
            elif vertex not in visited:
                visited.add(vertex)
                for neighbor, weight in graph[vertex]:
                    if neighbor not in visited:
                        stack.append((neighbor, product * weight))
        return -1
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []
        
        for equ in range(len(equations)):
            graph[equations[equ][0]].append([equations[equ][1], values[equ]])
            graph[equations[equ][1]].append([equations[equ][0], 1 / values[equ]])
        
        for query in queries:
            val = self.dfs(graph, query[0], query[1])
            ans.append(val)
        return ans