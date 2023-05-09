class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:            
        heap = []
        for pile in piles:
            heap.append(-pile)
        heapq.heapify(heap)
        
        for i in range(k):
            num = heapq.heappop(heap) * -1
            remove = math.ceil(num / 2) * -1
            heapq.heappush(heap, remove) 
        return sum(heap) * -1