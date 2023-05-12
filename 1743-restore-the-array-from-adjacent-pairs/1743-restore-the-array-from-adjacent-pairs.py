class Solution:    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        
        
        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
            
            indegree[num1] += 1
            indegree[num2] += 1
            
        for node in indegree:
            if indegree[node] == 1:
                queue.append((node,-1))
                break
        while queue:
            number, parent = queue.popleft()
            order.append(number)
            
            for neighbour in graph[number]:
                if neighbour != parent:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] <= 1:
                        queue.append((neighbour,number))
                
        return order
        