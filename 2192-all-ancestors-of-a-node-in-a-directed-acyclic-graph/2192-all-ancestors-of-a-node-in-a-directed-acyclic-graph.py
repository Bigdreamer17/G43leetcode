class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        answer = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        queue = deque()
        
        
        for num1, num2 in edges:
            graph[num1].append(num2)
            
            indegree[num2] += 1
            
        for num1 in range(n):
            if indegree[num1] == 0:
                queue.append(num1)
                
                
        while queue:
            node = queue.popleft()
            
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                
                answer[neighbour].add(node)
                answer[neighbour].update(answer[node])
                
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        for i in range(len(answer)):
            answer[i] = sorted(answer[i])
        return answer