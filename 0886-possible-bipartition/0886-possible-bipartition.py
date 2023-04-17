class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(i, color):
            if i in colors:
                return colors[i] == color
            colors[i] = color
            
            for neighbor in graph[i]:
                if not dfs(neighbor, 1-color):
                    return False
            return True
        
        graph = collections.defaultdict(list)
        colors = {}
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        for i in range(1,n+1):
            if i not in colors and not dfs(i, 0):
                return False
            
        return True