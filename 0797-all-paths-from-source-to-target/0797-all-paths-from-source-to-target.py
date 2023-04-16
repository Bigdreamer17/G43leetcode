class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(vertex, path):
            if path[-1] == len(graph) - 1:
                ans.append(path[:])
            
            for neighbour in graph[vertex]:
                path.append(neighbour)
                dfs(neighbour, path)
                path.pop()
                    
        dfs(0, [0])
        return ans
        