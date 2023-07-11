class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph,  seen  = defaultdict(list), set()
        
        for e,v in edges:
            graph[e].append(v)
            graph[v].append(e)
            
        def dfs(node):
            seen.add(node)
            
            ans  = sum(dfs(i) for i in graph[node] if i not in seen)
            
            if not ans and not hasApple[node]:
                return 0
            return ans + 2
        return max(0, dfs(0) - 2)