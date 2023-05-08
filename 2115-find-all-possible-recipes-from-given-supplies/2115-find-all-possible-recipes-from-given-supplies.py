class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        queue= deque()
        indegree = {}
        order = []
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] = 1 + indegree.get(recipes[i], 0)
        
        for sup in supplies:
            queue.append(sup)
            
                   
        while queue:
            node = queue.popleft()
            if node in recipes:
                order.append(node)
                
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return order
        
        
        
#         indegree = [node : 0 for in graph]
#         for node in graph:
#             for neighbor in graph[node]:
#                 indegree[neighbor] += 1
                
            