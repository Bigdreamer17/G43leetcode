class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        queue.append(0)
        visited = set()
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                
                for key in rooms[node]:
                    if key not in visited:
                        queue.append(key)
                        
        if len(visited) == len(rooms):
            return True
        else:
            return False