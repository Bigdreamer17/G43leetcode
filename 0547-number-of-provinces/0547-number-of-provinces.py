class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        visted = set()
        
        def dfs(graph, visted, vertex):
            visted.add(vertex)
            
            for neighbour in graph[vertex]:
                if neighbour not in visted:
                    dfs(graph, visted, neighbour)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[r])):
                if isConnected[r][c] != 0:
                    graph[r + 1].append(c + 1)
        count = 0
        for val in graph.keys():
            for i in graph[val]:
                if i not in visted:
                    count += 1
                    dfs(graph,visted, i)
        
        
                    
        
        return count