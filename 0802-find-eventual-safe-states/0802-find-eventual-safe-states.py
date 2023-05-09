class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        indegree = [0] * length
        adj = [[] for i in range(length)]
        
        for i in range(length): 
            indegree[i] = len(graph[i])
            for j in graph[i]:
                adj[j].append(i)
        
        queue = deque()
        order = []
        for i in range(length):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            order.append(node) 
            for i in adj[node]:
                if indegree[i]!=0:
                    indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return sorted(order)