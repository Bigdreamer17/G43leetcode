class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in range(len(matrix)):
            heap.extend(matrix[row])
        heapify(heap)
        while k > 0:
            ans = heappop(heap)
            k -= 1
            
        return ans