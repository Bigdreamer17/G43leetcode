class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        
        for src, des, dis in roads:
            graph[src].append((des, dis))
            graph[des].append((src, dis))
            
        queue = deque([1])
        visited = set([1])
        minDistance = float('inf')
        
        
        while queue:
            node = queue.popleft()
            
            
            for neighbour, distance in graph[node]:
                minDistance = min(minDistance, distance)
                
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        return minDistance