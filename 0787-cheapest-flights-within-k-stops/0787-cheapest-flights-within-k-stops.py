class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for fro, to, price in flights:
            graph[fro].append([to,price])
            
        heap = [(0 ,src, 0, -1)]
        cheapest = -1
        visited = set()
        while heap:
            cur_price, cur_city, stop_count, parent = heapq.heappop(heap)
            if cur_city == dst:
                cheapest = cur_price
                break
            
            if (cur_city, stop_count) in visited:
                continue
            
            visited.add((cur_city, stop_count))
            if stop_count > k:
                continue
            
            for city, price in graph[cur_city]:
                if (city, stop_count) not in visited:
                    heapq.heappush(heap, [cur_price + price, city, stop_count + 1, cur_city ])
                    
        return cheapest