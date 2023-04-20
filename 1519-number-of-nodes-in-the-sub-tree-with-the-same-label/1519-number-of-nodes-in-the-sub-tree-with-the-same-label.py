class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        counts = {}
        answer = [0] * n
        
        def dfs(node, parent):
            if labels[node] not in counts:
                counts[labels[node]] = 0

            previous = counts[labels[node]]
            counts[labels[node]] += 1
            
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    
            answer[node] = counts[labels[node]] - previous
        
        dfs(0, -1)
        return answer