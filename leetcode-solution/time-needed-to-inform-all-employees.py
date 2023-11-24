class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0

        graph = defaultdict(list)

        for i in range(n):
            if i != headID:
                graph[manager[i]].append(i)

        
        queue = deque()
        queue.append((headID, 0))
        visited = [0] * n
        visited[headID] = 1
        answer = 0

        while queue:
            node, time = queue.popleft()
            answer = max(answer, time)
            for nod in graph[node]:
                if visited[nod] == 0:
                    queue.append((nod, time + informTime[node]))
                    visited[nod] = 1

        return answer