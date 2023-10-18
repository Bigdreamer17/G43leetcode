class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        graph[0].append([firstPerson, 0])
        
        for p1, p2, time in meetings:
            graph[p1].append([p2, time])
            graph[p2].append([p1, time])
            
        
        minHeap = [[0, 0]]
        visited = set()
        
        
        while minHeap:
            prev, node = heappop(minHeap)
            if node in visited:
                continue
                
            visited.add(node)
            for child, cur in graph[node]:
                if cur >= prev:
                    heappush(minHeap, [cur, child])
                    
        return visited
            